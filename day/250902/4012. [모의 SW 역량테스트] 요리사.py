'''
    N/2개 나누어서 요리
    차이 최소
    넣고 넣기
'''
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = N//2
    foods = [list(map(int, input().split())) for _ in range(N)]

    mn = 1e9
    def dfs(n, alst, blst):
        global mn
        if n == N:
            if len(alst) == M:
                a, b = 0, 0
                for i in range(M): #0,1 1,0 둘 다 들어가게 range 설정
                    for j in range(M):
                        a += foods[alst[i]][alst[j]]
                        b += foods[blst[i]][blst[j]]
                mn = min(mn, abs(a-b))
            return

        dfs(n+1, alst + [n], blst)
        dfs(n+1, alst, blst+[n])

    dfs(0, [], [])

    print(f'{tc} {mn}')

