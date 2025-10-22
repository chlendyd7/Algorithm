'''
N개의 피자를 구울 수 있음
치즈가 모두 녹으면 꺼냄, 피자마다 다름
M개의 피자를 순서대로 화덕에 넣을 때
화덕 한바퀴 시 치즈 양은 반으로 줄어듬
모두 녹아 0이 되면 화덕에서 꺼냄
'''
from collections import deque


def solution():
    N, M = map(int, input().split())
    cheeses = list(map(int, input().split()))

    oven = deque()
    for i in range(N):
        oven.append((cheeses[i], idx+1))

    pizza_idx = N

    while len(oven) > 1:
        cheese, num = oven.popleft()
        cheese //= 2

        if cheese > 0:
            oven.append((cheese, num))
        elif pizza_idx < M:
            oven.append((cheeses[pizza_idx], pizza_idx + 1))
            pizza_idx += 1

    return oven[0][1]



T = int(input())
for tc in range(1, T+1):
    print(f'#{tc} {solution()}')
