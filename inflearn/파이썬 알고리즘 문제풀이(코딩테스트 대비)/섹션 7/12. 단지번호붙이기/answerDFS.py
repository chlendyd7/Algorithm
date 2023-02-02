dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def DFS(x, y):
    global cnt
    cnt+=1 # 왜 cnt +1 검증 안해도 되는가? 하나의 집 좌표가 발견되면 상관없기 때문
    board[x][y]=0 # 왜 바로 0으로 초기화? 중복방문 막기 위함 i와 j의 값은 이미 받아옴
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
            DFS(xx, yy)

if __name__=="__main__":
    n=int(input())
    board=[list(map(int, input())) for _ in range(n)] # 띄어쓰기가 없어 input()으로 한 줄 다 읽음
    res=[]
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                cnt=0
                DFS(i, j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)

