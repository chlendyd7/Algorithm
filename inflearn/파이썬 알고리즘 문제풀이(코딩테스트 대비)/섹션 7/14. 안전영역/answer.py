#다시보기
import sys
sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
sys.setrecursionlimit(10**6)# 시간 limit

def DFS(x, y, h):
    ch[x][y]=1
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=x<n and 0<=y<n and ch[xx][yy]==0 and board[xx][yy]>h:
            DFS(xx,yy,h)


    

if __name__=="__main__":
    n = int(input())
    cnt = 0
    res = 0
    board=[list(map(int, input().split())) for _ in range(n)]
    for h in range(100):
        ch=[[0]*n for _ in range(n)] # 새로운 판을 계속 만듬
        for i in range(n): #2중 for문 100번?
            for j in range(n):
                if ch[i][j]==0 and board[i][j]>h:
                    cnt+=1
                    DFS(i,j,h)






    