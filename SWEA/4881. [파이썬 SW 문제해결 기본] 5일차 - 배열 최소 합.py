'''
    하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
'''
def dfs(row, curr_sum):
    global min_sum
    
    if curr_sum >= min_sum:
        return

    if row == N:
        min_sum = min(min_sum, curr_sum)
        return

    for col in range(N):
        if not visited[col]:
            visited[col] = True
            dfs(row + 1, curr_sum + matrix[row][col])
            visited[col] = False


T = int(input())
for k in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_sum = float('inf')
    
    dfs(0, 0)
    print(f"#{k} {min_sum}")
