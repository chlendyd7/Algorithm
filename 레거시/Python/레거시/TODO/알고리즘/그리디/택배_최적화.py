from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

N, C = map(int, input().split())
M = int(input())
boxes = sorted([tuple(map(int,input().split())) for _ in range(M)])
arrivedBox = [0] * (N+1)
maxHeap = [] # 도착지점이 큰 거 빼내서 버리기
curTown = 0
curWeight = 0
result = 0
print(boxes)
for f, t, m in boxes:
    # 다음 지점으로 이동. 배송 물건 내려놓기.
    while curTown < f:
        curTown += 1
        result += arrivedBox[curTown]
        curWeight -= arrivedBox[curTown]
    print(arrivedBox)
    # 박스 싣기
    if curTown == f:
        heappush(maxHeap, -t)
        arrivedBox[t] += m
        curWeight += m
        
        while curWeight > C:
            destination = -heappop(maxHeap)
            amount = min(arrivedBox[destination], curWeight-C)
            arrivedBox[destination] -= amount
            curWeight -= amount
            if arrivedBox[destination]:
                heappush(maxHeap, -destination)
        
while curTown < N:
    curTown += 1
    result += arrivedBox[curTown]
    
print(result)