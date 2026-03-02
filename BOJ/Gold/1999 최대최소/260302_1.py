N, B, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
mx_row = [[0] * (N-B+1) for _ in range(N)]
mn_row = [[0] * (N-B+1) for _ in range(N)]

for r in range(N):
    for c in range(N-B+1):
        row = board[r][c:c+B]
        mx_row[r][c] = max(row)
        mn_row[r][c] = min(row)
# print(mx_row)
final_mx = [[0] * (N-B+1) for _ in range(N-B+1)]
final_mn = [[0] * (N-B+1) for _ in range(N-B+1)]

for r in range(N-B+1):
    for c in range(N-B+1):
        final_mx[r][c] = max(mx_row[r:r+B][c])
        final_mn[r][c] = min(mn_row[r:r+B][c])
# print(final_mx, '\n', final_mn)
for _ in range(K):
    i, j = map(int, input().split())
    i, j = i-1, j-1
    print(final_mx[i][j] - final_mn[i][j])


