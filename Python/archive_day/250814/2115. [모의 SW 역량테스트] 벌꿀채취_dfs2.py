def find_max_value(cell):
    max_value = 0
    
    def dfs(depth, honey, total_value):
        nonlocal max_value
        
        if honey > C:
            return

        if depth == M:
            max_value = max(max_value, total_value)
            return
        

        dfs(depth + 1, honey + cell[depth], total_value + cell[depth]**2)
        dfs(depth+1, honey, total_value)

    dfs(0, 0, 0)
    return max_value



def solution():

    values = []
    for i in range(N):
        for j in range(0, N-M+1):
            cell = board[i][j:j+M]
            honey_value = find_max_value(cell)
            values.append((i,j,honey_value))
    
    answer = 0
    for i in range(len(values)):
        r1, c1, p1 = values[i]
        for j in range(i + 1, len(values)):
            r2, c2, p2 = values[j]
            if r1== r2:
                if not (c1 + M <= 2 or c2 + M <= c1):
                    continue
            answer = max(answer, p1 + p2)
 
    return answer


T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t} {solution()}')
