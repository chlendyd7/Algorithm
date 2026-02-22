

N,L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

def check(line):
    visited = [False] * N

    for i in range(N-1):
        diff = line[i+1] - line[i]

        if diff == 0:
            continue

        if abs(diff) > 1:
            return False
        
        if diff == -1:
            for j in range(i+1, i+L+1):
                if j >= N or line[j] != line[i+1] or visited[j]:
                    return False
                visited[j] = True
        
        elif diff == 1:
            for j in range(i, i-L, -1):
                if j < 0 or line[i] != line[j] or visited[j]:
                    return False
            visited[j] = True

    return True

for r in range(N):
    col = [board[i][j] for i in range(N)]
    if check(board[r]):
        cnt += 1