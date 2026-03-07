import heapq

def elevator_with_heapq():
    curr_floor = 1
    direction = 1

    up_heap = []
    down_heap = []

    requests = [10,5,2,15,8]
    for r in requests:
        if r > curr_floor:
            heapq.heappush(up_heap, r)
        else:
            heapq.heappush(down_heap, -r)
    
    while up_heap or down_heap:
        if direction == 1:
            if up_heap:
                next_stop = heapq.heappop(up_heap)
                