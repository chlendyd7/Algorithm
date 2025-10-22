def solution():
    N, M = map(int, input().split())
    flag = [input().strip() for _ in range(N)]

    # 각 행마다 색칠 비용
    costW, costB, costR = [], [], []
    for row in flag:
        w = row.count('W')
        b = row.count('B')
        r = row.count('R')
        costW.append(M - w)
        costB.append(M - b)
        costR.append(M - r)

    # 누적합
    prefixW = [0] * N
    prefixB = [0] * N
    prefixR = [0] * N
    prefixW[0], prefixB[0], prefixR[0] = costW[0], costB[0], costR[0]

    for i in range(1, N):
        prefixW[i] = prefixW[i-1] + costW[i]
        prefixB[i] = prefixB[i-1] + costB[i]
        prefixR[i] = prefixR[i-1] + costR[i]

    ans = float('inf')

    # 경계 i, j 선택
    for i in range(N-2):         # W 끝
        for j in range(i+1, N-1):  # B 끝
            total = 0
            # W 영역
            total += prefixW[i]
            # B 영역
            total += prefixB[j] - prefixB[i]
            # R 영역
            total += prefixR[N-1] - prefixR[j]
            ans = min(ans, total)

    return ans


T = int(input())
for t in range(1, T+1):
    print(f"#{t} {solution()}")
