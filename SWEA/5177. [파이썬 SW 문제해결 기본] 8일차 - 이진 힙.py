class MinHeap:
    def __init__(self):
        self.heap = [0]

    def insert(self, val):
        self.heap.append(val)
        self._percolate_up(len(self.heap) - 1)
    
    def _percolate_up(self, idx):
        while idx > 1:
            parent = idx // 2
            if self.heap[parent] > self.heap[idx]:
                self.heap[parent], self.heap[idx] = self.heap[idx] , self.heap[parent]
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

heap = MinHeap()
for val in [3 ,1, 4 ,16, 23,12]:
    heap.insert(val)

print("조상 노드의 합:", heap.get_ancestor_sum())
