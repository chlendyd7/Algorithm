import sys
sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
    else:
        for k in range(4):
            xx=x+dx[k]
            yy=y+dy[k]
            if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>board[x][y]:
                ch[xx][yy]=1
                DFS(xx, yy)
                ch[xx][yy]=0

if __name__=="__main__":
    n=int(input())
    board=[[0]*n for _ in range(n)]
    ch=[[0]*n for _ in range(n)]
    max=-2147000000
    min=2147000000
    for i in range(n): # 0 ~ 4
        tmp=list(map(int, input().split())) # 한 줄을 읽음
        for j in range(n): 
            if tmp[j]<min: # 출발 지점1w
                min=tmp[j]
                sx=i
                sy=j
            if tmp[j]>max: # 도착지점
                max=tmp[j]
                ex=i
                ey=j      
            board[i][j]=tmp[j] # board에 한줄 복사해 넣음
    ch[sx][sy]=1 # 출발지점 좌표를 알게 됨
    cnt=0
    DFS(sx, sy)
    print(cnt)