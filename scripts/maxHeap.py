import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib
matplotlib.use('Agg')


class Node:
    def __init__(self, value):
        """
        Constructor de la clase Node
        Parameters
        ----------
        value
        """
        self.value = value
        self.left = None
        self.right = None


class MaxHeap:
    def __init__(self):
        """
        Constructor de la clase MaxHeap
        """
        self.root = None
        self.size = 0

    def insert(self, value):
        """
        Inserta un nuevo nodo en el heap
        Parameters
        ----------
        value
        Returns
        -------
        """
        if not self.root:
            self.root = Node(value)
            self.size += 1
            return

        node_queue = [self.root]
        while node_queue:
            current_node = node_queue[0]
            if not current_node.left:
                current_node.left = Node(value)
                self.size += 1
                self._heapify_up(current_node.left)
                return
            elif not current_node.right:
                current_node.right = Node(value)
                self.size += 1
                self._heapify_up(current_node.right)
                return
            else:
                node_queue.append(current_node.left)
                node_queue.append(current_node.right)
                node_queue.pop(0)

    def delete(self):
        """
        Elimina el nodo con mayor prioridad
        Returns
        -------
        Si el heap esta vacio retorna None, de lo contrario retorna el valor del nodo eliminado
        """
        if not self.root:
            return None

        deleted_value = self.root.value

        last_node = self._get_last_node()
        last_node_value = last_node.value
        self.root.value = last_node_value

        if self.size == 1:
            self.root = None
        else:
            parent = self._get_parent(last_node)
            if parent.right:
                parent.right = None
            else:
                parent.left = None
            self._heapify_down(self.root)

        self.size -= 1
        return deleted_value

    def _get_last_node(self):
        """
        Obtiene el ultimo nodo del heap
        Returns
        -------
        Si el heap esta vacio retorna None, de lo contrario retorna el ultimo nodo
        """
        if not self.root:
            return None
        current_node = None
        node_queue = [self.root]
        while node_queue:
            current_node = node_queue.pop(0)

            if current_node.left:
                node_queue.append(current_node.left)
            if current_node.right:
                node_queue.append(current_node.right)

        return current_node

    def _heapify_up(self, node):
        """
        Reordena el heap de abajo hacia arriba
        Parameters
        ----------
        node
        Returns
        -------
        Si el heap esta vacio retorna None, de lo contrario retorna el ultimo nodo
        """
        parent = self._get_parent(node)
        while parent and (int(node.value['priority']) > int(parent.value['priority']) or
                          (int(node.value['priority']) == int(parent.value['priority']) and
                           int(node.value['id']) > int(parent.value['id']))):
            self._swap_values(node, parent)
            node = parent
            parent = self._get_parent(node)

    def _swap_values(self, node1, node2):
        """
        Intercambia los valores de dos nodos
        Parameters
        ----------
        node1
        node2

        Returns
        -------
        """
        temp = node1.value
        node1.value = node2.value
        node2.value = temp

    def _heapify_down(self, node):
        """
        Reordena el heap de arriba hacia abajo
        Parameters
        ----------
        node

        Returns
        -------

        """
        while node:
            largest = node
            if node.left and (int(node.left.value['priority']) > int(largest.value['priority']) or
                              (int(node.left.value['priority']) == int(largest.value['priority']) and
                               int(node.left.value['id']) > int(largest.value['id']))):
                largest = node.left
            if node.right and (int(node.right.value['priority']) > int(largest.value['priority']) or
                               (int(node.right.value['priority']) == int(largest.value['priority']) and
                                int(node.right.value['id']) > int(largest.value['id']))):
                largest = node.right

            if largest != node:
                node.value, largest.value = largest.value, node.value
                node = largest
            else:
                break

    def _get_parent(self, node):
        """
        Obtiene el padre de un nodo
        Parameters
        ----------
        node

        Returns
        -------
        Si el nodo es la raiz retorna None, de lo contrario retorna el padre del nodo
        """
        node_queue = [self.root]
        while node_queue:
            current_node = node_queue.pop(0)

            if current_node.left == node or current_node.right == node:
                return current_node

            if current_node.left:
                node_queue.append(current_node.left)
            if current_node.right:
                node_queue.append(current_node.right)

    def delete_specific(self, id):
        """
        Elimina un nodo especifico
        Parameters
        ----------
        id
        Returns
        -------
        Si el heap esta vacio retorna None, de lo contrario retorna el valor del nodo eliminado
        """
        if not self.root:
            return None

        node_queue = [self.root]
        while node_queue:
            current_node = node_queue.pop(0)
            if current_node.value['id'] == id:
                last_node = self._get_last_node()
                last_node_value = last_node.value
                current_node.value = last_node_value

                if self.size == 1:
                    self.root = None
                else:
                    parent = self._get_parent(last_node)
                    if parent.right:
                        parent.right = None
                    else:
                        parent.left = None
                    self._heapify_down(self.root)

                self.size -= 1
                return current_node.value

            if current_node.left:
                node_queue.append(current_node.left)
            if current_node.right:
                node_queue.append(current_node.right)

        return None

    def get_node(self, id):
        """
        Obtiene un nodo especifico
        Parameters
        ----------
        id
        Returns
        -------
        Si el nodo existe, retorna el nodo, de lo contrario retorna None
        """
        if not self.root:
            return None

        node_queue = [self.root]
        while node_queue:
            current_node = node_queue.pop(0)
            if current_node.value['id'] == id:
                return current_node.value

            if current_node.left:
                node_queue.append(current_node.left)
            if current_node.right:
                node_queue.append(current_node.right)

        return None

    def get_sorted_elements(self):
        """
        Obtiene los elementos del heap ordenados
        Returns
        -------
        Si el heap esta vacio retorna None, de lo contrario retorna una lista con los elementos ordenados
        """
        sorted_elements = []
        heap_copy = MaxHeap()  # Creamos una copia del montículo original para no modificarlo

        # Extraemos los elementos del montículo original y los insertamos en la copia
        while self.size > 0:
            element = self.delete()
            sorted_elements.append(element)
            heap_copy.insert(element)

        # Restauramos el montículo original a partir de la copia
        self.root = heap_copy.root
        self.size = heap_copy.size

        return sorted_elements

    def visualize(self):
        """
        Visualiza el heap

        Returns
        -------
        Si el heap esta vacio retorna None, de lo contrario retorna una cadena en base64 con la imagen del heap
        """
        if not self.root:
            return

        sorted_elements = self.get_sorted_elements()

        # Crear una lista de etiquetas para los nodos
        labels = [f"id: {element['id']}" for element in sorted_elements]

        # Crear una lista de posiciones x para los nodos
        x_positions = list(range(len(sorted_elements)))

        # Configurar el tamaño de la figura
        plt.figure(figsize=(6, 1))

        # Dibujar los nodos como puntos en la posición x
        plt.scatter(x_positions, [0] * len(sorted_elements), marker='o', color='blue', s=200)

        # Agregar las etiquetas de los nodos
        for label, x, y in zip(labels, x_positions, [0] * len(sorted_elements)):
            plt.annotate(label, (x, y), xytext=(0, 10), textcoords='offset points', ha='center')

        # Configurar los límites de los ejes y ocultar los ejes
        plt.xlim(-1, len(sorted_elements))
        plt.ylim(-1, 1)
        plt.axis('off')

        # Guardar la figura en un buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.clf()

        # Convertir la imagen en base64
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        return image_base64

    def print(self):
        """
        Imprime los elementos del heap
        Returns
        -------
        Si el heap esta vacio retorna None, de lo contrario imprime los elementos del heap
        """
        if not self.root:
            return

        node_queue = [self.root]
        while node_queue:
            current_node = node_queue.pop(0)
            print(current_node.value, end=" ")
            if current_node.left:
                node_queue.append(current_node.left)
            if current_node.right:
                node_queue.append(current_node.right)
        print()


patientsMaxHeap = MaxHeap()

patientsMaxHeap.insert({
    'name': 'John',
    'id': "1",
    'priority': "1",
    'case': 'fever'
})

patientsMaxHeap.insert({
    'name': 'Jane',
    'id': "2",
    'priority': "2",
    'case': 'fever'
})

patientsMaxHeap.insert({
    'name': 'Mary',
    'id': "3",
    'priority': "3",
    'case': 'fever'
})

patientsMaxHeap.insert({
    'name': 'Peter',
    'id': "4",
    'priority': "4",
    'case': 'fever'
})

patientsMaxHeap.insert({
    'name': 'Harry',
    'id': "5",
    'priority': "5",
    'case': 'fever'
})
