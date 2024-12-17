import sys


dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
def DFS(x,y,h):
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>h:
            ch[xx][yy]=1
            DFS(xx,yy,h)

sys.setrecursionlimit(10**6)# 시간 limit


if __name__=="__main__":
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    res = 0

    for h in range(100):
        ch = [[0]*n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] >h and ch[i][j]==0:
                    cnt+=1
                    DFS(i,j,h)
        res = max(res, cnt)
        if cnt ==0:
            break
    print(res)