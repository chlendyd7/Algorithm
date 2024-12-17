import heapq


n = int(input())
cupNodle = [list(map(int, input().split())) for _ in range(n)]
cupNodle.sort()

arr = []
for i in range(1, n+1):
    heapq.heappush(arr, cupNodle[i])
    
    arr.append(cupNodle[i])
    if 