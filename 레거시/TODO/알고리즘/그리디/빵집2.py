import sys
sys.setrecursionlimit(100000)

# 입력
R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]

# 이동 방향: 위 대각선, 오른쪽, 아래 대각선
dy = [-1, 0, 1]

# 방문 여부를 체크하기 위한 배열
visited = [[False] * C for _ in range(R)]
result = 0

def dfs(y, x):
    if x == C - 1:
        return True  # 마지막 열에 도달하면 성공

    for i in range(3):
        ny = y + dy[i]
        nx = x + 1

        if 0 <= ny < R and not visited[ny][nx] and board[ny][nx] == '.':
            visited[ny][nx] = True  # 방문 체크
            if dfs(ny, nx):
                return True

    return False

# 첫 번째 열의 각 행에서 시작하여 파이프를 설치
for i in range(R):
    if board[i][0] == '.':
        visited[i][0] = True
        if dfs(i, 0):
            result += 1

# 결과 출력
print(result)
