'''
    
1
5 1000
100 200
300 500
250 300
500 1000
400 400
'''
def solution():
    N, L = map(int, input().split())
    ingredients = [tuple(map(int, input().split())) for _ in range(N)]
    
    dp = [0] * (L + 1)
    
    for score, cal in ingredients:
        for c in range(L, cal - 1, -1):  # 뒤에서부터 업데이트
            dp[c] = max(dp[c], dp[c - cal] + score)
    
    return max(dp)


T = int(input())
for t in range(1, T + 1):
    print(f'#{t} {solution()}')
