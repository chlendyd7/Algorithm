import sys
sys.stdin = open("input.txt", "r")

# n이 20이라 최대 뻗어나가는게 40칸 필요함 끝에서 끝
cost = [(k*k + (k-1) * (k-1)) for k in range(40)] #미리 cost를 계산해둠
def solve():
    ans = 0
    for si in range(N):
        for sj in range(N):     # 모든 시작위치
            for k in range(1, 2*N):
                cnt = 0
                for i in range(si-k+1, si+k): # 탐색하는 위치 row좌표
                    for j in range(sj-k+1+abs(i-si), sj+k-abs(i-si)): #범위정리
                        # 범위내이고 집인경우 count
                        if 0<=i<N and 0<=j<N and arr[i][j]:
                            cnt += 1

                # cost = k*k + (k-1)*(k-1)
                if cost[k] <= cnt*K and ans<cnt:
                    ans = cnt
    return ans

'''
    1. 모든 home 좌표 저장
    2. 모든 si, sj 기준으로 dist 생성
    
    
    
'''
def solve1():
    ans = 0
    home = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                home.append((i,j))

    # 모든 좌표를 순회하며 dist 만들어주기
    for si in range(N):
        for sj in range(N):
            dist = [0] * 40
            for h1, hj in home:
                t = abs(si-h1) + abs(sj-hj) + 1
                dist[t] += 1

            cnt = 0
            for k in range(1, 40):
                cnt += dist[k]
                if cost[k] <= cnt * K and ans < cnt:
                    ans = cnt
    return ans

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    ans = solve()
    # ans = solve1()
 
    print(f'#{test_case} {ans}')