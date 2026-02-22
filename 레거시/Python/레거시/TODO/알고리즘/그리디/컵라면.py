import heapq


n = int(input())
q = []
cup_laman = [list(map(int, input().split())) for _ in range(n)]
cup_laman.sort()
for i in cup_laman:
    heapq.heappush(q, i[1])
    if len(q) > i[0]:
        heapq.heappop(q)

print(sum(q))
