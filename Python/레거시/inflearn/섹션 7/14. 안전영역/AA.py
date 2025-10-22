#다시보기
import sys
#sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
sys.setrecursionlimit(10**6)# 시간 limit

def DFS(x, y, h):
    ch[x][y]=1 # 넘어온 x, y 좌표 방문 했다 체크
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>h: #board의 가려는 지점 h 보다 커야함
            DFS(xx,yy,h)


if __name__=="__main__":
    n = int(input())
    cnt = 0
    res = 0
    board=[list(map(int, input().split())) for _ in range(n)]
    for h in range(100):
        ch=[[0]*n for _ in range(n)] # 새로운 판을 계속 만듬
        cnt =0
        for i in range(n): #2중 for문 100번?
            for j in range(n):
                if ch[i][j]==0 and board[i][j]>h:
                    cnt+=1
                    DFS(i,j,h)# 좌표 넘기기, 더 뻣을 곳이 없으면 돌아옴 2중for문 계속
        res=max(res, cnt) # res보다 cnt 보다 크면
        if cnt==0: # cnt가 0이면 for문 멈춤
            break
    print(res)


