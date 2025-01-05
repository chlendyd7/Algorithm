def solution(n, results):
    graph = [[] * (n+1) for _ in range(n+1)]
    for w, l in results:
        graph[w][l] = True
    
    
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                if graph[i][j] or graph[j][k]:
                    graph[i][k] = True
    
    answer = 0
    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if graph[i][j] or graph[j][i]:
                count += 1
        if count == n -1:
            answer += 1
    
    
    
    return answer