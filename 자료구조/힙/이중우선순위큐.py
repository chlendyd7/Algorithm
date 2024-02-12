import heapq

def solution(operations):
    max_heap = []
    min_heap = []
    
    for op in operations:
        command, value = op.split()
        value = int(value)
        
        if command == "I":
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
        elif command == "D":
            if not max_heap:
                continue
            
            if value==1:
                min_heap.remove(-heapq.heappop(max_heap))
                heapq.heapify(max_heap)
            
            if value==-1:
                max_heap.remove(-heapq.heappop(min_heap))
                heapq.heapify(min_heap)
        if not min_heap:
            return [0, 0]
    else:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]