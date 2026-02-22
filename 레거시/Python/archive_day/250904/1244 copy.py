'''
    자리 교환 가능
    교환 횟수는 2
    오른쪽이 1
    왼쪽이 10배수만큼 커짐
    동일한 위치의 교환이 중복되어도 된다..?
'''
from collections import defaultdict
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    ans = 0
    board, M = input().split()
    board = list(board)
    N = len(board)
    dp = defaultdict(list)
    def dfs(n, value):
        global ans

        key = tuple(value)
        if key in dp[n]:
            return
        dp[n].append(key)

        if n == int(M):
            tmp = int(''.join(value))
            ans = max(ans, int(tmp))
            return

        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                value[i], value[j] = value[j], value[i]
                dfs(n+1, value)
                value[i], value[j] = value[j], value[i]

    dfs(0, board)
    print(f'#{tc} {ans}')
