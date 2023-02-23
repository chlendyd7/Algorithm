import sys
import heapq as hq
from collections import defaultdict
input=sys.stdin.readline

for _ in range(int(input())):
    maxQ, minQ = [], []
    check=defaultdict(int)
    for _ in range(int(input())):
        cmd, n = input().split()
        if cmd=="I":
            hq.heappush(maxQ, -int(n))
            hq.heappush(minQ, int(n))
            check[int(n)]+=1
        elif n=="1":
            while maxQ and check[-maxQ[0]]==0:
                hq.heappop(maxQ)
            if maxQ:
                check[-maxQ[0]]-=1
                hq.heappop(maxQ)
        elif n=="-1":
            while minQ and check[minQ[0]]==0:
                hq.heappop(minQ)
            if minQ:
                check[minQ[0]]-=1
                hq.heappop(minQ)
    while maxQ and check[-maxQ[0]]==0:
        hq.heappop(maxQ)
    while minQ and check[minQ[0]]==0:
        hq.heappop(minQ)
    if maxQ and minQ:
        print(-maxQ[0], minQ[0])
    else:
        print("EMPTY")
