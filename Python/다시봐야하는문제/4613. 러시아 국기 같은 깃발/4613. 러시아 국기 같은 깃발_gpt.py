def solution():
    N, M = map(int, input().split())
    flag = [input().strip() for _ in range(N)]

    # 각 행마다 특정 색으로 바꾸는 데 필요한 비용 계산
    cost = []
    for row in flag:
        w = row.count('W')
        b = row.count('B')
        r = row.count('R')
        # W로 칠할 비용 = 전체 - W 개수
        cost.append({
            'W': M - w,
            'B': M - b,
            'R': M - r
        })

    ans = float('inf')

    # 흰색은 0~i행, 파랑은 i+1~j행, 빨강은 j+1~N-1행
    for i in range(N - 2):          # W 끝나는 위치
        for j in range(i + 1, N - 1):  # B 끝나는 위치
            total = 0
            # 흰색 부분
            for k in range(0, i + 1):
                total += cost[k]['W']
            # 파랑 부분
            for k in range(i + 1, j + 1):
                total += cost[k]['B']
            # 빨강 부분
            for k in range(j + 1, N):
                total += cost[k]['R']
            ans = min(ans, total)

    return ans


T = int(input())
for t in range(1, T + 1):
    print(f"#{t} {solution()}")
