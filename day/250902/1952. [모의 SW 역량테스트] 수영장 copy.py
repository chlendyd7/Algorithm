T = int(input())
for tc in range(1, T+1):
    day, month, month3, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    D = [0] * 13

    for i in range(1, 13):
        D[i] = D[i-1] + plan[i] * day
        D[i] = min(D[i], D[i-1] + month)
        if i >= 3:
            D[i] = min(D[i], D[i-3] + month3)
        if i == 12:
            D[i] = min(D[i], D[i-12] + year)
    print(f'#{tc} {D[12]}')
