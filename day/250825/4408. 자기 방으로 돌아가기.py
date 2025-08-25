def solution():
    N = int(input())
    room = [0] * 201
    for _ in range(N):
        start, end = map(int, input().split())
        for r in range(start//2, end//2+1):
            room[r] += 1

    return max(room)


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
