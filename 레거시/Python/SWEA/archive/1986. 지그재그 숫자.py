def solution():
    N = int(input())
    if N % 2:
        return N - (1 * (N // 2))
    else:
        return -1 * (N // 2)


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
