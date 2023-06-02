from django.shortcuts import render
from scripts.maxHeap import patientsMaxHeap


# Create your views here.


def create_patient(request):
    """
    Esta función se encarga de crear un paciente y agregarlo al heap de pacientes.
    Parameters
    ----------
    request

    Returns
    -------
    El render de la página de creación de pacientes con el paciente creado y el heap visualizado.

    """
    context = {}
    if request.method == 'POST':

        if request.POST.get('months') == "":
            months = 0
        else:
            months = int(request.POST.get('months'))
        if request.POST.get('age') == "":
            age = 0
        else:
            age = int(request.POST.get('age'))

        age = age + (months/12)

        patient = {'name': request.POST.get('name'),
                   'age': age,
                   'date': {'months': request.POST.get('months'), 'year': request.POST.get('age')},
                   'id': request.POST.get('id'),
                   'priority': request.POST.get('priority')
                   }

        if request.POST.get('case') == "":
            patient['case'] = "Caso sin especificar"
        else:
            patient['case'] = request.POST.get('case')

        patientsMaxHeap.insert(patient)
        context['patient'] = patient

    context['image'] = patientsMaxHeap.visualize()

    return render(request, 'heap_creation_template/heap_creation_form.html', context)


def get_appointment(request):
    """
    Esta función se encarga de obtener el paciente con mayor prioridad y eliminarlo del heap.
    Parameters
    ----------
    request

    Returns
    -------
    El render de la página de obtención de citas con el paciente obtenido y el heap visualizado.

    """
    context = {}
    if request.method == 'POST':
        patient = patientsMaxHeap.delete()
        print(patient)
        if patient is not None:
            context['patient'] = patient

    context['image'] = patientsMaxHeap.visualize()

    return render(request, 'get_appointment_template/get_appointment_form.html', context)


def modify_patient(request):
    """
    Esta función se encarga de modificar un paciente y actualizarlo en el heap.
    Parameters
    ----------
    request

    Returns
    -------
    El render de la página de modificación de pacientes con el paciente modificado y el heap visualizado.

    """
    context = {}
    if request.method == 'GET':
        patient_id = request.GET.get('search-id')
        if patient_id is not None:
            patient = patientsMaxHeap.get_node(patient_id)
            if patient is not None:
                context['patient'] = patient

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'modify_patient':
            if request.POST.get('modify-months') == "":
                months = 0
            else:
                months = int(request.POST.get('modify-months'))
            if request.POST.get('modify-age') == "":
                age = 0
            else:
                age = int(request.POST.get('modify-age'))

            age = age + (months / 12)

            aux_patient = {
                'name': request.POST.get('modify-name'),
                'age': age,
                'date': {'months': request.POST.get('modify-months'), 'year': request.POST.get('modify-age')},
                'id': request.POST.get('hidden-id'),
                'priority': request.POST.get('modify-priority'),
                'case': request.POST.get('modify-case')
            }

            patientsMaxHeap.delete_specific(aux_patient['id'])
            patientsMaxHeap.insert(aux_patient)

        elif form_type == 'delete_patient':
            patient_id = request.POST.get('delete_id')
            if patient_id is not None:
                deleted_patient = patientsMaxHeap.delete_specific(patient_id)
                if deleted_patient is not None:
                    context['deleted_patient'] = deleted_patient
                    context['message'] = "success"
                else:
                    context['message'] = "error"

    context['image'] = patientsMaxHeap.visualize()

    context['prioritys_array'] = [i for i in range(1, 6)]

    return render(request, 'modify_patient_template/modify_patient_form.html', context)
