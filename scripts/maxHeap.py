import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib
matplotlib.use('Agg')


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class MaxHeap:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
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
        parent = self._get_parent(node)
        while parent and (int(node.value['priority']) > int(parent.value['priority']) or
                          (int(node.value['priority']) == int(parent.value['priority']) and
                           int(node.value['id']) > int(parent.value['id']))):
            self._swap_values(node, parent)
            node = parent
            parent = self._get_parent(node)

    def _swap_values(self, node1, node2):
        temp = node1.value
        node1.value = node2.value
        node2.value = temp

    def _heapify_down(self, node):
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

    def visualiz2(self):
        if not self.root:
            return

        fig, ax = plt.subplots()
        self._plot_node(ax, self.root, 0, 0, 0.8)
        ax.axis('off')
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.clf()

        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()
        return image_base64

    def visualize(self):
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

    def _plot_node(self, ax, node, x, y, level):
        if not node:
            return

        ax.annotate(f"id: {node.value['id']}\npr: {node.value['priority']}",
                    (x, y),
                    ha='center',
                    va='center',
                    bbox=dict(facecolor='white', edgecolor='black'))

        if node.left:
            x_left = x - 0.5 / (2 ** level)
            y_left = y - 1
            ax.plot([x, x_left], [y, y_left], '-k')
            self._plot_node(ax, node.left, x_left, y_left, level + 1)

        if node.right:
            x_right = x + 0.5 / (2 ** level)
            y_right = y - 1
            ax.plot([x, x_right], [y, y_right], '-k')
            self._plot_node(ax, node.right, x_right, y_right, level + 1)

    def convert_to_max_heap(self):
        if not self.root:
            return

        node_queue = [self.root]
        while node_queue:
            current_node = node_queue.pop(0)
            self._heapify_down(current_node)
            if current_node.left:
                node_queue.append(current_node.left)
            if current_node.right:
                node_queue.append(current_node.right)

    def print(self):
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

patientsMaxHeap.print()
