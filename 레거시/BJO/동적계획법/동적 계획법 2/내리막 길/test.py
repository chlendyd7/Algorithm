import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    # 목적지에 도달한 경우 경로 1개 추가
    if x == M-1 and y == N-1:
        return 1
    
    # 이미 계산된 경로가 있는 경우 해당 경로 수 반환
    if dp[x][y] != -1:
        return dp[x][y]
    
    # 경로 수 초기화
    dp[x][y] = 0
    
    # 이동 방향 정의 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        # 지도 범위를 벗어나지 않으면서 더 낮은 높이로 이동할 수 있는 경우
        if 0 <= nx < M and 0 <= ny < N and height_map[nx][ny] < height_map[x][y]:
            dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

# 입력 받기
M, N = map(int, input().split())
height_map = [list(map(int, input().split())) for _ in range(M)]

# DP 테이블 초기화 (-1로 초기화하여 아직 방문하지 않은 상태 표시)
dp = [[-1] * N for _ in range(M)]

# 결과 출력
print(dfs(0, 0))