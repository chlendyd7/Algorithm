from collections import defaultdict

def solution(sales, links):
    n = len(sales)
    tree = defaultdict(list)
    
    # 트리 구성
    for parent, child in links:
        tree[parent - 1].append(child - 1)

    # DP 배열: dp[node][0] - 참석하지 않음, dp[node][1] - 참석
    dp = [[0, 0] for _ in range(n)]
    visited = [False] * n

    def dfs(node):
        visited[node] = True
        dp[node][1] = sales[node]  # node 참석 시 초기값
        
        extra_cost = float('inf')  # 부하 중 최소 추가 비용
        for child in tree[node]:
            if not visited[child]:
                dfs(child)
                # 최소 피로도 갱신
                dp[node][0] += min(dp[child][0], dp[child][1])  # 부모 불참
                dp[node][1] += min(dp[child][0], dp[child][1])  # 부모 참석

                # 자식이 회의에 참석하지 않는 경우의 추가 비용
                extra_cost = min(extra_cost, dp[child][1] - min(dp[child][0], dp[child][1]))
        
        # 부모가 불참할 경우 자식 중 하나는 반드시 참석해야 함
        if extra_cost != float('inf'):
            dp[node][0] += extra_cost

    # 루트에서 DFS 시작
    dfs(0)

    # 최소값 반환
    return min(dp[0][0], dp[0][1])
