def solution():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 괴물 위치 찾기 (문제 조건상 괴물 한 마리)
    monster_x, monster_y = -1, -1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                monster_x, monster_y = i, j
                break
        if monster_x != -1:
            break

    # 상하좌우 방향 벡터
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    # 광선 쏘기
    for dx, dy in directions:
        x, y = monster_x, monster_y
        while True:
            x += dx
            y += dy
            if x < 0 or x >= N or y < 0 or y >= N:
                break
            if board[x][y] == 1 or board[x][y] == 2:  # 벽 또는 괴물 만나면 종료
                break
            if board[x][y] == 0:
                board[x][y] = 3  # 위험한 칸 표시

    # 안전한 칸(0) 개수 세기
    safe_count = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                safe_count += 1

    return safe_count


T = int(input())
for t in range(1, T+1):
    print(f"#{t} {solution()}")
