import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
direction = [(0,1), (-1,0), (0,-1), (1,0)]
board = [[0] * 101 for _ in range(101)]

for _ in range(N):
    c, r, d, g = map(int, input().split())
    direct = [d]
    for _ in range(g):
        for i in range(len(direct)-1, -1, -1):
            direct.append((direct[i]+1)%4)

    board[r][c] = 1
    for d in direct:
        nr, nc = direction[d]
        board[r+nr][c+nc] = 1
        r += nr
        c += nc

cnt = 0
for i in range(101):
    for j in range(101):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            cnt += 1
print(cnt)

# print(input())
