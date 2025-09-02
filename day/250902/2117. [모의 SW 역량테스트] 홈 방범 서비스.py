cost = [(k*k + (k-1) * (k-1)) for k in range(40)]
def solve():
    ans = 0
    for sr in range(N):
        for sc in range(N):
            for k in range(1, 2*N):
                cnt = 0
                for i in range(sr-k+1, sr+k):
                    for j in range(sc-k+1+abs(i-sr), sc + k -abs(i-sr)):
                        if 0<= i < N and 0 <= j < N and arr[i][j]:
                            cnt += 1
                if cost[k] <= cnt * K and ans < cnt:
                    ans = cnt

    return ans

def solve1():
    ans = 0
    home = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                home.append((i, j))
    
    for sr in range(N):
        for sc in range(N):
            dist = [0] * 40
            for h1, hj in home:
                t = abs(sr-h1) + abs(sc-hj) + 1
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
 
    # ans = solve()
    ans = solve1()
 
    print(f'#{test_case} {ans}')
