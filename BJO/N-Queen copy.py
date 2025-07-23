def dfs(row):
    if row == N:
        global answer
        answer += 1
        return

    for col in range(N):
        if v1[col] == v2[row + col] == v3[row - col] == 0:
            v1[col] = v2[row + col] = v3[row - col] = 1
            dfs(row+1)
            v1[col] = v2[row + col] = v3[row - col] = 0

N = int(input())
answer = 0
v1 = [0] * N
v2 = [0] * (2*N)
v3 = [0] * (2*N)
dfs(0)
print(answer)


def is_valid(row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def dfs(row):
    if row == N:
        global answer
        answer += 1
        return
    for col in range(N):
        if is_valid(row, col):
            board[row] = col
            dfs(row + 1)

N = int(input())
answer = 0
board = [0] * N
dfs(0)
print(answer)
