# ChallengeHospitalAJMA
Este proyecto es parte de un conjunto de programas que se desarrollaron como parte para la empresa AJMA.
Este programa utiliza el TDA de Montículos para modelar un sistema de prioridad de un hospital en la sala de urgencias.

## Tabla de contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Créditos](#créditos)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Instalación

### 1. Abre una terminal:
Algunos comandos son:
- Windows: "Windows + R" para abrir el cuadro de diálogo Ejecutar, luego escribe "cmd" y presiona Enter.
- MacOS: "Command + Barra espaciadora", luego escribiendo "Terminal" y presiona Enter.
- Linux: "Ctrl + Alt + T"
### 2. Clona el repositorio a tu máquina local: 
- git clone https://github.com/EstructuraDeDatosUSB/ChallengeHospitalAJMA.git
### 3. Accede al directorio:
- cd ChallengeHospitalAJMA
### 4. Crear un entorno virtual (Opcional - Si deseas no llenar tu máquina local de librerías):
- pip install virtualenv
- mkdir venv
- cd venv

#### - En Windows:
- venv\Scripts\activate

#### - En macOS y Linux:
- source venv/bin/activate
  
### 5. Instala los requerimientos
- pip install -r requirements.txt


## Uso

### 1. Abra la terminal en el proyecto
### 2. Inicia el servidor de desarrollo de Django
- python manage.py runserver

## Características

### TDA Maxheap:
- Permite insertar elementos en el montículo.
- Mantiene los elementos en orden de prioridad, donde el elemento de mayor prioridad se encuentra en la raíz del montículo.
- Permite eliminar el elemento de mayor prioridad (raíz) del montículo.
- Permite obtener el nodo con un ID específico.
- Permite eliminar un nodo con un ID específico.
- Proporciona una representación visual del montículo en forma de árbol.
- Permite convertir el montículo en un MaxHeap válido.
- Permite obtener una lista ordenada de elementos del montículo en orden descendente de prioridad.

- Además, se utiliza la biblioteca matplotlib para generar visualizaciones del montículo en forma de árbol.

- En el ejemplo de código proporcionado, se crea una instancia de la clase MaxHeap llamada patientsMaxHeap y se realizan algunas operaciones de inserción. Luego se imprime el montículo resultante.

### TDA Minheap:
Cada nodo contiene un valor y enlaces a sus hijos izquierdo y derecho.
- Permite insertar valores en el heap.
- Mantiene los elementos en orden de prioridad, donde el elemento de menor prioridad se encuentra en la raíz del heap.
- Permite eliminar el elemento de menor prioridad (raíz) del heap.
- Permite obtener el último nodo del heap.
- Permite realizar el proceso de heapify hacia arriba, intercambiando un nodo con su padre si el valor del nodo es menor que el de su padre.
- Permite realizar el proceso de heapify hacia abajo, intercambiando un nodo con su hijo más pequeño si el valor del nodo es mayor que el de su hijo más pequeño.
- Permite obtener el padre de un nodo dado.
- Permite imprimir el heap en orden de nivel.

### Aplicacion:
- Se usa el TDA Maxheap
- Permite agregar nuevos pacientes al sistema.
- Permite asignar una prioridad a cada paciente en su creación.
- Permite editar la prioridad de un paciente ya existente.
- Permite actualizar la prioridad de un paciente existente.
- Permite la eliminacion de un paciente
- Permite atender un paciente.
- Proporciona una lista ordenada de pacientes en base a su prioridad.
- Ofrece una interfaz de usuario intuitiva y fácil de usar.

## Créditos

Este proyecto fue desarrollado por los siguientes miembros de la organización EstructuraDeDatosUSB en Github:

- Gustavo Camargo (Dueño de la organización)
- Dillan Asprilla
- Mariana Cruz
- Juan Manuel Conde
- Jhon Mario Diaz
- Juan David Diaz

Agradecemos a todos los miembros de la organización por su contribución a este proyecto

## Licencia

Este proyecto se encuentra bajo la siguiente licencia:

[![Licencia CC-BY-NC-ND 4.0](https://i.creativecommons.org/l/by-nc-nd/4.0/80x15.png)](http://creativecommons.org/licenses/by-nc-nd/4.0/deed.es)

El contenido de este proyecto está protegido por la licencia Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internacional. Esto significa que puedes utilizar y compartir este proyecto con otros bajo las siguientes condiciones:

- *Atribución (Attribution):* Debes otorgar crédito adecuado, proporcionando un enlace a la licencia y mencionando a los autores originales.
- *No Comercial (NonCommercial):* No puedes utilizar este proyecto con fines comerciales.
- *No Derivados (NoDerivatives):* No puedes modificar, adaptar o crear obras derivadas a partir de este proyecto.

Para obtener más información sobre los términos y condiciones de esta licencia, puedes visitar el siguiente enlace: [Licencia CC-BY-NC-ND 4.0](http://creativecommons.org/licenses/by-nc-nd/4.0/deed.es).
