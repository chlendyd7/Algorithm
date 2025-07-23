def solution():
    n = int(input())
    speed = 0
    distance = 0
    for _ in range(n):
        go = list(map(int, input().split()))
        if go[0] == 1:
            speed += go[1]
        elif go[0] == 2:
            speed -= go[1]
            if speed < 0:
                speed = 0
    
        distance += speed

    return distance


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')