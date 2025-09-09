import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bullons = list(map(int, input().split()))
    ans = -1

    def dfs(n, value, bullons:list):
        global ans
        if n == N:
            ans = max(ans, value)
            return


        lst_len = len(bullons)
        for i in range(lst_len):
            if lst_len == 1:
                dfs(n+1, value + bullons[i], [])

            if i == 0:
                value += bullons[i]
            elif i == lst_len - 1:
                value += bullons[i-1]
            else:
                value += bullons[i-1] * bullons[i+1]
            tmp = bullons.pop(i)
            dfs(n+1, value, bullons)
            bullons.insert(i, tmp)
    dfs(0, 0, bullons)
    print(f'#{tc} {ans}')
