'''
    최대값 찾기
    N명 N개의 일
    그리디 아님
'''
def solution():
    N = int(input())
    best_val = 0
    visited = [0] * N
    data = [list(map(int, input().split())) for _ in range(N)]

    def dfs(depth, val):
        nonlocal best_val
        if depth == N:
            best_val = max(best_val, val)
            return
        
        if val <= best_val:
            return

        for i in range(N):
            if visited[i]:
                continue
            visited[i] = 1
            dfs(depth+1, val * data[depth][i] / 100)
            visited[i] = 0

    dfs(0, 1)
    return f'{best_val*100:.6f}'


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')