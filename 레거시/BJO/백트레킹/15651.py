import sys
input = sys.stdin.readline

n,m = map(int, input().split())
ls = []

def dfs():
    if len(ls)==m:
        print(' '.join(map(str, ls)))
        return
    for i in range(1, n+1):
        ls.append(i)
        dfs()
        ls.pop()

dfs()
