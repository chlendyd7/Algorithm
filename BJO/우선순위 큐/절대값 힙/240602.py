import sys, heapq as hq

input = sys.stdin.readline

n = int(input())
ls = []
for _ in range(n):
    num = int(input())
    if num == 0:
        print(hq.heappop(ls)[1] if ls else 0)
    else:
        hq.heappush(ls, (abs(num), num))

