def solution():
    n = int(input())
    rocks = list(map(int, input().split()))
    mn = 1e9
    cnt = 0
    for rock in rocks:
        if abs(rock) < mn:
            mn = abs(rock)
            cnt = 1
        elif abs(rock) == mn:
            cnt += 1
    return mn, cnt


T = int(input())
for t in range(1, T+1):
    mn, cnt = solution()
    print(f'#{t} {mn} {cnt}')