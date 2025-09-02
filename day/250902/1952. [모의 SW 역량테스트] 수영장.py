T = int(input())
for tc in range(1, T+1):
    day, month, month3, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    days = [0] * 13

    day = 0
    for i in range(1, 13):
        days[i] = day[i-1] + plan[i] * day
        day[i] = min(day[i], day[i-1] + month)
        
    

    ans = 1e9
    def dfs(n, value):
        global ans
        if n >= 12:
            ans = min(ans, value)
            return
        
        nxt = n+1
        dfs(nxt, value+plan[nxt] * day)
        dfs(nxt, value+month)
        dfs(n+3, value+month3)
        dfs(n+12, value+year)
    dfs(0, 0)
    print(f'#{tc} {ans}')

