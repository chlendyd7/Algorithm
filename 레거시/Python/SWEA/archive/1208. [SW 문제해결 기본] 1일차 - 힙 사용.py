import heapq


def solution():
    dump_cnt = int(input())
    boxs = list(map(int, input().split()))
    max_heap = [-b for b in boxs]
    min_heap = boxs[:]
    
    heapq.heapify(max_heap)
    heapq.heapify(min_heap)
    
    for _ in range(dump_cnt):
        max_val = -heapq.heappop(max_heap)
        min_val = heapq.heappop(min_heap)
        
        if max_val - min_val <= 1:
            heapq.heappush(max_heap, -max_val)
            heapq.heappush(min_heap, min_val)
            break
        
        max_val -= 1
        min_val += 1

        heapq.heappush(max_heap, -max_val)
        heapq.heappush(min_heap, min_val)

    return -heapq.heappop(max_heap) - heapq.heappop(min_heap)

for t in range(1, 11):
    print(f'#{t} {solution()}')