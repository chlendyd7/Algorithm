import sys
sys.setrecursionlimit(100000)

def solution(n, lighthouse):
    dp = [[0]*2 for _ in range(n)]
    node_dict = { key : [] for key in range(n) }
    visited = [False]*n
    for a, b in lighthouse :
        node_dict[a-1].append(b-1)
        node_dict[b-1].append(a-1)
        
    def dfs(node) :
        visited[node] = True
        leaf_list = list()
        for leaf in node_dict[node] :
            if visited[leaf] :
                continue
            leaf_list.append(leaf)
            dfs(leaf)

        dp[node][0] = 0
        dp[node][1] = 1
# 출처: https://magentino.tistory.com/43 [마젠티노's:티스토리]
