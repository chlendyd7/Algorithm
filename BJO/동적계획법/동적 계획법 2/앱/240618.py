def min_cost_to_free_memory(N, M, memories, costs):
    # 가능한 최대 비용 (N개 앱의 최대 비용 합)
    max_cost = sum(costs)
    
    # DP 배열 초기화: 비용을 index로 하는 배열, 확보 가능한 메모리 저장
    dp = [0] * (max_cost + 1)
    
    # DP 업데이트
    for i in range(N):
        mem = memories[i]
        cost = costs[i]
        # 뒤에서부터 업데이트하여 중복 방지
        for j in range(max_cost, cost - 1, -1):
            dp[j] = max(dp[j], dp[j - cost] + mem)
    
    # 최소 비용 찾기
    for cost in range(max_cost + 1):
        if dp[cost] >= M:
            return cost

    return -1  # 이 경우는 주어진 조건에서 발생하지 않음

# 입력 받기
N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

# 결과 출력
print(min_cost_to_free_memory(N, M, memories, costs))
