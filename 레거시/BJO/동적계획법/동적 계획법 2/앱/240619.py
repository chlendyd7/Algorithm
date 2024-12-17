def min_cost_to_free_memory(N, M, memories, costs):
    max_cost = sum(costs)
    dp = [0] * (max_cost + 1)
    
    for i in range(N):
        memory = memories[i]
        cost = costs[i]
        
        for j in range(max_cost, cost -1, -1):
            dp[j] = max(dp[j], dp[j-cost] + memory)
        
    for k in range(max_cost + 1):
        if dp[k] >= M:
            return k
    return -1

N,M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
print(min_cost_to_free_memory(N,M,memories,costs))
