import heapq


n, k = map(int, input().split())
jewaly = []
for _ in range(n):
    heapq.heappush(jewaly, list(map(int, input().split())))
bags = [int(input()) for _ in range(k)]
bags.sort()

answer = 0
tmp_jew = []
for bag in bags:
    while jewaly and bag >= jewaly[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jewaly)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    elif not jewaly:
        break

print(answer)
