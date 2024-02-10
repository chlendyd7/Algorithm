import heapq

def solution(scoville, K):
    heapq.heapify(scoville) #힙 자료형으로 만들어줌
    
    mix_count = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        new_scovile = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new_scovile)
        
        mix_count +=1
    
    return mix_count