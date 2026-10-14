# https://atcoder.jp/contests/dp/tasks/dp_u
def solve():
    N = int(input())
    a = []
    for _ in range(N):
        row = list(map(int, input().split()))
        a.append(row)
    
    # 부분집합의 점수 계산
    def calc_score(mask):
        score = 0
        for i in range(N):
            if not (mask & (1 << i)):
                continue
            for j in range(i + 1, N):
                if not (mask & (1 << j)):
                    continue
                score += a[i][j]
        return score
    
    # DP
    dp = [-float('inf')] * (1 << N)
    dp[0] = 0
    
    for mask in range(1 << N):
        if dp[mask] == -float('inf'):
            continue
        
        # mask에 포함되지 않은 토끼 중 가장 작은 번호
        remaining = ((1 << N) - 1) ^ mask
        if remaining == 0:
            continue
        
        first_bit = remaining & (-remaining)  # 가장 낮은 비트
        
        # first_bit을 포함하는 모든 부분집합 시도
        subset = remaining
        while subset > 0:
            if subset & first_bit:  # first_bit 포함해야 함
                new_mask = mask | subset
                score = calc_score(subset)
                dp[new_mask] = max(dp[new_mask], dp[mask] + score)
            subset = (subset - 1) & remaining
    
    return dp[(1 << N) - 1]

print(solve())
