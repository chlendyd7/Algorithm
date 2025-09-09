dy = [-1,1,0,0]
dx = [0,0,-1,1]

types = {
    # 상하좌우 기록
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited =[[0] * M for _ in range(N)]
    