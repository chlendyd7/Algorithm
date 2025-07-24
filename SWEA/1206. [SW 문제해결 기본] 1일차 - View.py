def solution():
    n = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0
    for i in range(2, n-1):
        now = buildings[i]
        check_point = sorted(buildings[i-2: i+3], reverse=True)
        if now == check_point[0]:
            cnt += now - check_point[1]
    return cnt

for t in range(1, 11):
    print(f'#{t} {solution()}')


def solution():
    n = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0
    for i in range(2, n - 2):
        now = buildings[i]
        max_neighbor = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
        if now > max_neighbor:
            cnt += now - max_neighbor
    return cnt

for t in range(1, 11):
    print(f'#{t} {solution()}')