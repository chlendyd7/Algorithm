def solution():
    N, M =map(int, input().split())
    rocks = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        idx = i - 1
        left = idx - 1
        right = idx + 1
        for _ in range(j):
            if 0 > left or right >= N:
                break

            if rocks[left] == rocks[right]:
                if rocks[left]:
                    rocks[left], rocks[right] = 0, 0
                else:
                    rocks[left], rocks[right] = 1, 1
            left -=1
            right +=1 

    return ' '.join(map(str, rocks))


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
