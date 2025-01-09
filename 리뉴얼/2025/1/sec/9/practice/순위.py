def solution(n, results):
    graph = [[False] * (n+1) for _ in range(n+1)]
    for win, lose in results:
        graph[win][lose] = True
    
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True
    
    answer = 0
    for i in range(n+1):
        temp_cnt = 0
        for j in range(n+1):
            if graph[i][j] or graph[j][i]:
                temp_cnt += 1
        
        if temp_cnt == n - 1:
            answer += 1
    return answer