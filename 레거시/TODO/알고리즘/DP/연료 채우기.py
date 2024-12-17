import heapq


n = int(input())
oil_station = [list(map(int, input().split())) for _ in range(n)]
P, L = list(map(int, input().split()))
oil_station.append([P, 0])

oil_station.sort(key=lambda x:(x[0], -x[1]))
oil_heap = []
cnt = 0
for p, l in oil_station:
    if L >= P:
        break
    while oil_heap and P < l:
        P += -heapq.heappop(oil_heap)
        cnt += 1
    if P < l:
        break
    heapq.heappush(oil_heap, -p)

print(cnt if P >= L else -1)
