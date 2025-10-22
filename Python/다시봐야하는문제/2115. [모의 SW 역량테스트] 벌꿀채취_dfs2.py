# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V4A46AdIDFAWu
def get_max_profit(cells, C):
    """
    재귀를 이용한 부분집합 탐색으로
    꿀 양 합이 C 이하인 부분집합 중 꿀 양 제곱합 최대값 구하기
    """
    max_profit = 0
    M = len(cells)

    def dfs(idx, total_honey, total_profit):
        nonlocal max_profit
        if total_honey > C:
            return
        if idx == M:
            max_profit = max(max_profit, total_profit)
            return
        # 포함하는 경우
        dfs(idx + 1, total_honey + cells[idx], total_profit + cells[idx]**2)
        
        # 포함하지 않는 경우(모든 조합을 찾기 위해) (단순 제곱)
        dfs(idx + 1, total_honey, total_profit)

    dfs(0, 0, 0)
    return max_profit

def solution():
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    segments = []
    for r in range(N):
        for c in range(N - M + 1):
            cells = board[r][c:c + M]
            profit = get_max_profit(cells, C)
            segments.append((r, c, profit))

    answer = 0
    for i in range(len(segments)):
        r1, c1, p1 = segments[i]
        for j in range(i + 1, len(segments)):
            r2, c2, p2 = segments[j]
            if r1 == r2 and not (c1 + M <= c2 or c2 + M <= c1):
                continue
            answer = max(answer, p1 + p2)

    return answer

T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solution()}")
