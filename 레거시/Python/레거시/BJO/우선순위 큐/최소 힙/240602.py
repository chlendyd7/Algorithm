import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
ls = []

for _ in range(n):
    num = int(input())
    if num == 0:
        print(hq.heappop(ls) if ls else 0)
    else:
        hq.heappush(ls, num)
