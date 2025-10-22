def solution():
    N = int(input())
    nums = list(input())
    mx = 0
    cnt = 0
    for n in nums:
        if int(n):
            cnt += 1
        else:
            mx = max(cnt, mx)
            cnt = 0

    return max(mx, cnt)


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
