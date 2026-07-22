def solution():
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    
    # dp[mask] = mask 비트로 표현된 일들을 배분했을 때의 최대 확률
    dp = [0.0] * (1 << n)
    dp[0] = 1.0  # 아무것도 배분 안 함: 확률 100%
    
    # 모든 상태를 순회
    for mask in range(1 << n):
        if dp[mask] == 0:  # 도달 불가능한 상태
            continue
        
        # 이 상태에서 다음 직원이 누구인지 확인
        current_worker = bin(mask).count('1')
        
        if current_worker == n:  # 모든 직원이 일을 배분받음
            continue
        
        # 아직 배분 안 된 일들을 현재 직원에게 배분
        for job in range(n):
            if mask & (1 << job) == 0:  # job이 아직 배분 안 됨
                next_mask = mask | (1 << job)
                probability = lst[current_worker][job] / 100
                dp[next_mask] = max(
                    dp[next_mask],
                    dp[mask] * probability
                )
    
    # 모든 일이 배분된 경우의 최대 확률
    max_probability = dp[(1 << n) - 1]
    percentage = max_probability * 100
    
    return f'{percentage:.6f}'

T = int(input())
for t in range(1, T + 1):
    result = solution()
    print(f'#{t} {result}')

print