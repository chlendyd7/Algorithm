def get_max_profit(cells, C):
    """
    주어진 벌통 리스트에서 C 이하로 꿀을 채취할 때 얻을 수 있는 최대 수익(제곱합)
    부분집합 탐색 (브루트포스)
    """
    M = len(cells)
    max_profit = 0
    for mask in range(1, 1 << M):
        total_honey = 0
        total_profit = 0
        for i in range(M):
            if mask & (1 << i):
                total_honey += cells[i]
                total_profit += cells[i] ** 2
        if total_honey <= C:
            max_profit = max(max_profit, total_profit)
    return max_profit


def solution():
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 1. 가능한 모든 선택 구간과 그 최대 수익 미리 계산
    segments = []
    for r in range(N):
        for c in range(N - M + 1):
            cells = board[r][c:c + M]
            profit = get_max_profit(cells, C)
            segments.append((r, c, profit))

    # 2. 두 구간 선택해서 최대 수익
    answer = 0
    for i in range(len(segments)):
        r1, c1, p1 = segments[i]
        for j in range(i + 1, len(segments)):
            r2, c2, p2 = segments[j]
            # 겹치지 않는 조건
            if r1 == r2 and not (c1 + M <= c2 or c2 + M <= c1):
                continue
            answer = max(answer, p1 + p2)

    return answer


T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solution()}")