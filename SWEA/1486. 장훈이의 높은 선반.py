'''
    선반의 높이 B
    N명의 점원
'''
def solution():
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    max_height = sum(heights)
    dp = [False] * (max_height + 1)
    dp[0] = True
    for h in heights:
        for i in range(max_height, -1, -1):
            if dp[i]:
                dp[h + i] = True
    b = B
    while True:
        if dp[b]:
            return b - B
        b += 1


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
