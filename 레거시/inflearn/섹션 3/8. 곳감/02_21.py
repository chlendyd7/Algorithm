n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    a, b, c = map(int,input().split())
    
    if b == 0:
        for _ in range(c):
            board[a-1].append(board[a-1].pop(0))
    else:
        for _ in range(c):
            board[a-1].insert(0, board[a-1].pop())

cnt = 0
lt = 0
rt = n #5
for i in range(n):
    for j in range(lt, rt):
        cnt += board[i][j]
    
    if i < n//2:
        lt +=1
        rt -=1
    
    else:
        lt -=1
        rt +=1
print(cnt)