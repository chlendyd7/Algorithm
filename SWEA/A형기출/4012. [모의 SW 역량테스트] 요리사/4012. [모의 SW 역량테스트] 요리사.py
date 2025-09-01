#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH
'''
    맛의 차이가 최소가 되도록 재료를 분배
    i,j를 하면 시너지 발생
    ij는 시너지 합
    N <= 16

    백 트래킹유형: 모든 선택 완료 후 정답 처리해야함
'''


def dfs(n, alst, blst):
    global ans
    if n == N:
        if len(alst) == M:
            asum = bsum = 0
            for i in range(M):
                for j in range(M):
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            
            ans = min(ans, abs(asum - bsum))
        return

    dfs(n+1, alst+[n], blst)
    dfs(n+1, alst, blst+[n])

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    M = N//2 #자주사용됨(크기를 비교하기 위해) 절반 재료를 사용하니까
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 20000*N*N
    
    dfs(0, [], [])