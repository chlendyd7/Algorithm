import sys
sys.setrecursionlimit(10000)

def check(x, y, row, col):
    return 0 <= x < col and 0 <= y < row

dy = [-1, 0, 1]  # 오른쪽 위 대각선, 오른쪽, 오른쪽 아래 대각선

def dfs(x, y):
    if x == C - 1:  # 오른쪽 끝에 도달했으면 True
        return True
    
    for i in range(3):  # 세 가지 방향으로 이동
        nx = x + 1
        ny = y + dy[i]
        if check(nx, ny, R, C):  # 범위 확인
            if graph[ny][nx] == '.':  # 갈 수 있는 곳이면
                graph[ny][nx] = 'x'  # 방문 표시
                if dfs(nx, ny):  # 끝까지 도달하면 True 리턴
                    return True
    return False

R, C = map(int, input().split())  # 행, 열 입력
graph = [list(input()) for _ in range(R)]  # 그래프 입력

cnt = 0
for y in range(R):  # 첫 번째 열에서 각 행마다 시도
    if dfs(0, y):  # 각 행에서 시작
        cnt += 1
print(cnt)
