n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
prefix = [[0] * (n+1) for _ in range(n+1)]

def sum_prefix(r1, c1, r2, c2):
    return prefix[r2+1][c2+1] - prefix[r2+1][c1] - prefix[r1][c2+1] + prefix[r1][c1]

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix[i][j] = board[i-1][j-1] - prefix[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1]

ans = 0
for i in range(n-1):
    for j in range(n-1):
        sums =
print(prefix)