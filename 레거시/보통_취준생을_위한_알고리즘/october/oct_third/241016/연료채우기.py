import heapq


n = int(input())
cnt = 0
oil_bank = [list(map(int, input().split())) for _ in range(n)]
L,P = map(int, input().split())
oil_bank.append([L, 0])
oil_heap = []
oil_bank.sort(key=lambda x:(x[0], -x[1]))

for l, p in oil_bank:
    if P >= L:
        break
    while oil_heap and  P < l:
        P += -heapq.heappop(oil_heap)
        cnt += 1
    if P < l:
        break
    heapq.heappush(oil_heap, -p)
print(cnt if P >= L else -1)
