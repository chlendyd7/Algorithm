N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
T = int(input())

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        temp = []
        for r in range(i, i+3):
            for c in range(j, j+3):
                temp.append(board[r][c])
        temp.sort()
        if temp[4] >= T:
            cnt += 1

print(cnt)
