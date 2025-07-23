def backtrack(row):
    if row == N:
        global cnt
        cnt += 1
        return

    for i in range(i, N+1):
        if not row[i] and not col[i]:
            row[i] = 1
            col[i] = 1
            cnt += 1
            backtrack(i)
            row[i] = 0
            col[i] = 0

N = int(input())
cnt = 0
board = [[0] * N for _ in range(N)]
row = [0] * N
col = [0] * N
backtrack(0)
print(cnt)