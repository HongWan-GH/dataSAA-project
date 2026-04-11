class MaxHeap:
    """
    Task 2 Data Structure: MaxHeap. Not taught in the generic course.
    Finds the Top N most profitable stocks efficiently.
    O(n) build time, O(log n) extract time.
    """
    def __init__(self):
        self.heap = []

    def parent(self, index: int) -> int:
        return (index - 1) // 2

    def left_child(self, index: int) -> int:
        return 2 * index + 1

    def right_child(self, index: int) -> int:
        return 2 * index + 2

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index: int):
        while index > 0 and self.heap[self.parent(index)].profit < self.heap[index].profit:
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
            
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_down(self, index: int):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left].profit > self.heap[largest].profit:
            largest = left
        if right < len(self.heap) and self.heap[right].profit > self.heap[largest].profit:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    def get_top_n(self, n: int):
        top_elements = []
        for _ in range(min(n, len(self.heap))):
            top_elements.append(self.extract_max())
        return top_elements
