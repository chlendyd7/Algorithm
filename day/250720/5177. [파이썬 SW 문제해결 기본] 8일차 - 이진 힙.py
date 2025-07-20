class MinHeap:
    def __init__(self):
        self.heap = [0]

    def insert(self, val):
        self.heap.append(val)

    def _percolate_up(self, idx):
        while idx > 1:
            parent = idx // 2
            if self.heap[parent] > self.heap[idx]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = parent
            else:
                break

    def get_ancestor_sum(self):
        idx = len(self.heap) - 1
        total = 0
        while idx > 1:
            idx //= 2
            total += self.heap[idx]
        return total
