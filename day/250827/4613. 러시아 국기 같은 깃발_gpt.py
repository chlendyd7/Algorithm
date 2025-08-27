def solution():
    N, M = map(int, input().split())
    flag = [input().strip() for _ in range(N)]
    
    cost = []
    for row in flag:
        w = row.count('W')
        b = row.count('B')
        r = row.count('R')
        
        cost.append({
            'W': M-w,
            'B': M-b,
            'R': M-r,
        })
        
    ans = 1e9
    for i in range(N-2):
        for j in range(i+1, N-1):
            total = 0
            for k in range(i+1):
                total += cost[k]['W']
            for k in range(i+1, j+1):
                total += cost[k]['B']
            for k in range(j+1, N):
                total += cost[k]['R']
            ans = min(ans, total)
    return ans
T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solution()}")
