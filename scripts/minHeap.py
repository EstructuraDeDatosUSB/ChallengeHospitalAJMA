"""
This is a heap ADT, which is a complete binary tree that is either a min-heap or a max-heap.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class MinHeap:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            self.size += 1
            return

        # Perform a level-order traversal to find the first available position
        node_queue = [self.root]
        while node_queue:
            current_node = node_queue[0]
            if not current_node.left:
                current_node.left = Node(value)
                self.size += 1
                return
            elif not current_node.right:
                current_node.right = Node(value)
                self.size += 1
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

        node_queue = [self.root]
        while node_queue:
            current_node = node_queue.pop(0)

            if current_node.left:
                node_queue.append(current_node.left)
            if current_node.right:
                node_queue.append(current_node.right)

        return current_node

    def _heapify_up(self, node):
        while node != self.root:
            parent = self._get_parent(node)
            if node.value < parent.value:
                node.value, parent.value = parent.value, node.value
            node = parent

    def _heapify_down(self, node):
        while node:
            smallest = node
            if node.left and node.left.value < smallest.value:
                smallest = node.left
            if node.right and node.right.value < smallest.value:
                smallest = node.right

            if smallest != node:
                node.value, smallest.value = smallest.value, node.value
                node = smallest
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

    def prioritize_heap(self, mode):
        if mode == 'min':
            self._convert_to_min_heap()

    def _convert_to_min_heap(self):
        if not self.root:
            return

        node_queue = [self.root]
        while node_queue:
            current_node = node_queue.pop(0)
            smallest = current_node
            if current_node.left and current_node.left.value < smallest.value:
                smallest = current_node.left
            if current_node.right and current_node.right.value < smallest.value:
                smallest = current_node.right
            if smallest != current_node:
                current_node.value, smallest.value = smallest.value, current_node.value
                node_queue.append(smallest)
                # Continue heapifying down from the swapped child node
                node_queue.append(current_node)
                self._heapify_down(current_node)



# Test
heap = MinHeap()

heap.insert(5)
heap.insert(3)
heap.insert(4)
heap.insert(1)
heap.insert(2)
heap.insert(7)
heap.insert(6)
heap.insert(8)
heap.insert(9)
heap.insert(10)
heap.insert(11)
heap.insert(12)
heap.insert(13)

heap.prioritize_heap('min')

heap.print()
