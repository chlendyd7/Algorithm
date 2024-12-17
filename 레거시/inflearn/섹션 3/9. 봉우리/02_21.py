dx = [-1,0,1,0]
dy = [0,-1,0,1]
n=int(input())
board = [list(map(int,input().split())) for _ in range(n)]

board.insert(0,[0]*n)
board.append([0]*n)

for x in board: # 1차원만 돔
    x.insert(0,0) # 앞 1
    x.append(0) # 뒤 1

cnt =0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(board[i][j]>board[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)