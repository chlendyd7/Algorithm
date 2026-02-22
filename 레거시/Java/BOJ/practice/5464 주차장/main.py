from collections import deque


N, M = map(int, input().split())
park_price = []
for _ in range(N):
    park_price.append(int(input()))

car_weight = []
for _ in range(M):
    car_weight.append(int(input()))

q = deque()
parking = [0] * N
result = 0
log = dict()
for i in range(M*2):
    cmd = int(input())
    if q:
        for j in range(N):
            if not parking[j]: #parking이 0이면
                parking[j] = True
                car = q.popleft()
                log[car] = j #해당 차는 j에 주차
                result += car_weight[car-1] * park_price[j]
                break

    if cmd > 0:
        q.append(cmd)
    else:
        cmd = abs(cmd)
        parking[log[cmd]] = False

print(result)