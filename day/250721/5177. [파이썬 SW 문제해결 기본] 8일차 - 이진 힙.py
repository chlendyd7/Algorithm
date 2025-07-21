class MinHeap:
    def __init__(self):
        self.heap = [0]
    
    def insert(self, val):
        self.heap.append(val)
        self._percolate_up(len(self.heap) - 1)
    
    def _percolate_up(self, idx):
        #Percolate: 삼투
        while idx > 1:
            parent = idx // 2
            if self.heap[parent] > self.heap[idx]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = parent
            else:
                break

    def parent_sum(self):
        idx = len(self.heap) - 1
        total = 0
        while idx > 1:
            idx //= 2
            total += self.heap[idx]
        return total

T = int(input())
for t in range(1, T+1):
    heap = MinHeap()
    for val in list(map(int, input().split())):
        heap.insert(val)
    print(f'#{t} {heap.parent_sum()}')


