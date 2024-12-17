'''
1번은 올리기 n번은 내리기
'''
from collections import deque

def solution(n, k, belt_durable):
    step = 0
    belt = deque([False] * n)
    while True:
        step += 1

        belt_durable.rotate(1)
        belt.rotate(1)
        
        belt[n - 1] = False

        for i in range(n-2, -1, -1):
            if belt[i] and not belt[i+1] and belt_durable[i]:
                belt[i] = False
                belt[i+1] = True
                belt_durable[i] -= 1

        belt[n -1] = False
        if belt_durable[0] > 0:
            belt[0] = True
            belt_durable[0] -= 1

        if belt_durable.count(0) >= k:
            return step

n,k = map(int, input().split())
belt_durable = deque(list(map(int,input().split())))
print(solution(n,k,belt_durable))
