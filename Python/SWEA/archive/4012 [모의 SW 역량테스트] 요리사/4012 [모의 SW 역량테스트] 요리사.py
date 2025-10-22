# import os
# import sys


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 실행 중인 파일의 절대 경로
# sys.stdin = open(os.path.join(BASE_DIR, 'input.txt'), 'r')


def solution():
    N = int(input())
    M = N//2
    synerg = [list(map(int, input().split())) for _ in range(N)]
    
    result = 1e9
    visited = [0] * N

    def dfs(cnt, a: list, b: list):
        nonlocal result

        if cnt == N:
            if len(a) == N//2:
                asum = bsum = 0
                for i in range(M):
                    for j in range(M):
                        asum += synerg[a[i]][a[j]]
                        bsum += synerg[b[i]][b[j]]
                result = min(result, abs(asum - bsum))
            return

        dfs(cnt+1, a+[cnt], b)
        dfs(cnt+1, a, b+[cnt])
    dfs(0, [], [])

    return result


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
