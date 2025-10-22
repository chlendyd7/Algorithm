import sys
input = sys.stdin.readline

n,m = map(int, input().split())
ls = []

def dfs(start):
    if len(ls)==m:
        print(' '.join(map(str, ls)))
        return
    for i in range(start, n+1):
        ls.append(i)
        dfs(i)
        ls.pop()

dfs(1)