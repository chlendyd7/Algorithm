import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bullons = list(map(int, input().split()))
    ans = -1

    def dfs(n, value, visited):
        global ans
        if n == N:
            ans = max(ans, value)
            return

        for i in range(1, N):
            if visited[i]:
                continue
            left, right = i, i
            visited[i] = 1
            while left > 0 and visited[left]:
                left -= 1
            while right < N and visited[right]:
                right += 1

            if not left and right == N:
                dfs(n+1, value+bullons[i], visited)
            elif not left and right < N:
                dfs(n+1, value+bullons[right], visited)
            elif right == N:
                dfs(n+1, value+bullons[left], visited)
            else:
                dfs(n+1, value+(bullons[left] * bullons[right]), visited)
            visited[i] = 0

    visited = [0] * (len(bullons) + 1)
    dfs(0, 0, visited)
    print(f'#{tc} {ans}')
