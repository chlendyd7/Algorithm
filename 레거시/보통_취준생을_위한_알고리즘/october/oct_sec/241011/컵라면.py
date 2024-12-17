import heapq

n = int(input())
cup_nodle = [list(map(int, input().split())) for _ in range(n)]
cup_nodle.sort()
arr = []

for i in range(n):
    heapq.heappush(arr, cup_nodle[i][1])
    if len(arr) > cup_nodle[i][0]:
        heapq.heappop(arr)

print(sum(arr))
