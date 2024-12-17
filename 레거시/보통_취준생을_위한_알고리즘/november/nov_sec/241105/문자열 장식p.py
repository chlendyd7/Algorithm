import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def solution():
    N = int(input())
    heap = []
    M = 0
    for i in range(N):
        word = input().rstrip()
        heappush(heap, word+'_')
        M += len(word)
    res = ''
    for _ in range(M):
        word = heappop(heap)
        res += word[0]
        heappush(heap, word[1:])
    print(res)

solution()
