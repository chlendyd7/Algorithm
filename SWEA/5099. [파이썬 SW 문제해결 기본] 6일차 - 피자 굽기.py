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
    lst = list(map(int, input().split()))

    pizza_q = deque()
    for idx, pizza in enumerate(lst):
        pizza_q.append((pizza, idx+1))

    oven = deque()
    while len(oven) != 1:
        while len(oven) < N and pizza_q:
            oven.append(pizza_q.popleft())

        pizza, idx = oven.popleft()
        pizza //= 2
        if pizza:
            oven.append((pizza, idx))

    return oven[0][1]



T = int(input())
for tc in range(1, T+1):
    print(f'#{tc} {solution()}')
