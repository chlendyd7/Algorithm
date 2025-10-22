import sys
# 바뀌는거 x,y값 사다리는 오른쪽이나 왼쪽 한 방향으로만 이동
def DFS(x, y):
    ch[x][y]=1
    if x==0: # 시작하는 지점
        print(y)
    else:
        if y-1>=0 and board[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x, y-1)
        elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)


board=[list(map(int, input().split())) for _ in range(10)]
ch=[[0]*10 for _ in range(10)]
for y in range(10):
    if board[9][y]==2:
        DFS(9, y)