import sys
input = sys.stdin.readline

N,B = map(int, input().split())
A = [[*map(int ,input().split())] for _ in range(N)]

def mul(U,V):
    n = len(U)
    Z = [[0] * n for _ ]