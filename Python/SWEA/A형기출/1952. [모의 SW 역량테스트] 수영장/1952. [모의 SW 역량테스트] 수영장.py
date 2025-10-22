# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq&
# import sys
# sys.stdin = open('input.txt', 'r')
def dfs(n, sm):
    global ans
    if ans<=sm:
        return

    if n>12:
        ans = min(ans, sm)
        return

    dfs(n+1, sm+day*lst[n]) # 일간권
    dfs(n+1, sm+mon)        # 월간권
    dfs(n+3, sm+mon3)       # 분기권
    dfs(n+12, sm+year)      # 년간권

T = int(input())
for test_case in range(1, T + 1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))
    
    D = [0] * 13
    for i in range(1, 13):
        mn = D[i-1] + lst[i] * day
        mn = min(mn, D[i-1] + mon)
        if i >= 3:
            mn = min(mn, D[i-3] + mon3)
        if i >= 12:
            mn = min(mn, D[i-12] + year)
        
        D[i] = mn
    ans = D[12]

    print(f'#{test_case} {ans}')
