n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
mx = 0
sum3, sum4 = [0,0]
for i in range(n):
    sum1, sum2 = [0, 0]
    sum3 += board[i][i]
    sum4 += board[i][n - i - 1]
    for j in range(n):
        sum1 += board[i][j]
        sum2 += board[j][i]
    mx = max(mx, max(sum1, sum2, sum3, sum4))

print(mx)