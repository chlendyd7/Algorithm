def solve():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        scores = list(map(int, input().split()))

        # 최대 점수 합
        max_sum = sum(scores)
        dp = [False] * (max_sum + 1)
        dp[0] = True  # 0점 가능

        for p in scores:
            # 뒤에서부터 갱신 (중복 사용 방지)
            for s in range(max_sum, -1, -1):
                print('s:', s, dp[s])
                if dp[s]:
                    print('이거 맞음')
                    dp[s + p] = True

        # 가능한 점수의 개수
        result = sum(dp)
        print(f"#{t} {result}")

solve()
