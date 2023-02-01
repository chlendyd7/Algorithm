




# if __name__=="__main__":
#     dx = [-1,0,1,0]
#     dy = [0,1,0,1]
#     cnt=0
#     a = int(input())
#     mount = [list(map(int,input().split()))for _ in range(a)]
#     goal = max(mount)
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def DFS(x,y):
    global cnt
    if x==ex and y==ey: # 도착했으면 +1
        cnt+=1
    else:
        for k in range(4):
            xx=x+dx[k]
            yy=y+dy[k]
            if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>board[x][y]:
                ch[xx][yy]=1
                DFS(xx,yy)
                ch[xx][yy]=0


if __name__=="__main__":
    n=int(input())
    board=[[0]*n for _ in range(n)]
    ch=[[0]*n for _ in range(n)]
    max=-214700000
    min=214700000
    for i in range(n):
        tmp=list(map(int,input().split())) #입력되는 한 열을 읽으면서
        for j in range(n):
            if tmp[j]<min:
                min = tmp[j] # 작은 값의 좌표를 남겨두기
                sx = i
                sy = j
            if tmp[j]>max: # 큰 값의 좌표를 남겨두기
                max = tmp[j]
                ex = i
                ey = j
            board[i][j]=tmp[j] # 각 값을 append
    ch[sx][sy]=1 
    cnt=0
    DFS(sx,sy)
    print(cnt)

        