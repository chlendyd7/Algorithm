def solution():
    n = int(input())
    data = list(map(int, input().split()))

    # 회사
    sx, sy = data[0], data[1]

    # 집
    ex, ey = data[2], data[3]

    # 고객
    customers = []
    for i in range(4, 2 * n + 4, 2):
        customers.append((data[i], data[i + 1]))

    visited = [False] * n
    answer = float('inf')

    def dfs(count, cx, cy, dist):
        nonlocal answer

        # 가지치기:
        # 현재 거리만으로도 기존 최단 거리 이상이면 중단
        if dist >= answer:
            return

        # 모든 고객을 방문한 경우: 집까지 이동
        if count == n:
            dist += abs(cx - ex) + abs(cy - ey)
            answer = min(answer, dist)
            return

        # 아직 방문하지 않은 고객을 다음 목적지로 선택
        for i in range(n):
            if not visited[i]:
                nx, ny = customers[i]

                visited[i] = True

                next_dist = dist + abs(cx - nx) + abs(cy - ny)
                dfs(count + 1, nx, ny, next_dist)

                visited[i] = False

    dfs(0, sx, sy, 0)

    return answer


T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc} {solution()}')
