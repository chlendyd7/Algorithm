n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
m = 0
for i in range(n):
    sum1 = sum2= 0
    for j in range(n):
        sum1 += board[i][j]
        sum2 += board[j][i]
        if max(sum1,sum2) > m:
            m = max(sum1, sum2)

sum1 = sum2 = 0
for i in range(n):
    sum1 += board[i][i]
    sum2 += board[i][n-i-1]
    if max(sum1, sum2) > m:
        m = max(sum1, sum2)

print(m)