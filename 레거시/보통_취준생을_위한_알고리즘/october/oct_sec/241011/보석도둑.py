import heapq


n,k = map(int, input().split())
jew = []
for _ in range(n):
    heapq.heappush(jew, list(map(int, input().split())))
bags = [int(input()) for _ in range(k)]
bags.sort()
tmp_jew = []
answer = 0
for bag in bags:
    while jew and bag >= jew[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    elif not jew:
        break
print(answer)
