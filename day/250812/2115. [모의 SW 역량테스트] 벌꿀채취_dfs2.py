def find_max_honey(cells, C):
    max_honey = 0
    M = len(cells)

    def dfs(idx, total_honey, total_profit):
        nonlocal max_honey
        if total_honey > C:
            return
        if idx == M:
            max_honey = max(max_honey, total_profit)
            return

        dfs(idx + 1, total_honey + cells[idx], total_profit + cells[idx] ** 2)
        dfs(idx + 1, total_honey, total_profit)
    
    dfs(0, 0, 0)
    return max_honey
    
def solution():
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    segments = []
    for r in range(N):
        for c in range(N):
            cells = board[r][c:c+M]
            profit = find_max_honey(cells, C)
            segments.append((r, c, profit))
    answer = 0
    for i in range(len(segments)):
        r1, c1, p1 = segments[i]
        for j in range(1+1, len(segments)):
            r2, c2, p2 = segments[j]
            if r1 == r2 and not (c1 + M <= c2 or c2 + M <= c1):
                continue
            answer = max(answer, p1 + p2)

    return answer


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')