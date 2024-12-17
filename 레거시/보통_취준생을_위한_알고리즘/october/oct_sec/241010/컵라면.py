import heapq


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

q = []
cnt = 0
for a in arr:
    heapq.heappush(q, a[1])
    if len(q) > a[0]:
        heapq.heappop(q)
print(sum(q))
