#스타트와 링크 12/26
import sys
input = sys.stdin.readline

def dfs(depth, idx):
    global n, res
    if depth == n//2: #짝수가 되기 위해서
        p1, p2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]: #여기부터 다시 보기
                    p1 += s[i][j]
                elif not visit[i] and not visit[j]:
                    p2 += s[i][j]
        res = min(res, abs(p1-p2))
        return

    for i in range(idx,n):
        if not visit[i]:
            visit[i] = 1
            dfs(depth+1, i+1)
            visit[i] = 0


n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
visit = [0] * n
res = 1e3
dfs(0, 0)
print(res)