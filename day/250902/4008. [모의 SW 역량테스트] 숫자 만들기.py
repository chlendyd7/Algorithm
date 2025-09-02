# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    plus, minus, mul, div = map(int, input().split())
    nums = list(map(int, input().split()))

    mx = int(-1e9)
    mn = int(1e9)
    def dfs(n, value, p, m, mul, div):
        global mx, mn
        if n == N:
            mx = max(mx, value)
            mn = min(mn, value)
            return
    
        next = n+1
        if p:
            dfs(next, value+nums[n], p-1, m, mul, div)
        if m:
            dfs(next, value-nums[n], p, m-1, mul, div)
        if mul:
            dfs(next, value * nums[n], p, m, mul-1, div)
        if div:
            dfs(next, int(value / nums[n]), p, m, mul, div-1)


    dfs(1, nums[0], plus, minus, mul, div)
    print(f'#{tc} {mx - mn}')

