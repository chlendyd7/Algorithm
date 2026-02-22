def solution(n, computers):
    def dfs(node):
        visitied[node] = True
        for i, connected in enumerate(computers[node]):
            if connected and not visitied[i]:
                dfs(i)

    visitied = [False] * n
    count = 0

    for i in range(n):
        if not visitied[i]:
            dfs(i)
            count += 1
    
    return count
