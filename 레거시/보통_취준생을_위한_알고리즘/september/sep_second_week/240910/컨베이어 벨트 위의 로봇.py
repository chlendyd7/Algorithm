# 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
'''
    3n개가 있음
'''
from collections import deque
import sys

def solution(N, K, A):
    answer = 0
    belt = deque([False] * N)
    
    while True:
        answer += 1

        A.rotate(1)
        belt.rotate(1)

        belt[N-1] = False
        for i in range(N-2, -1, -1):
            if belt[i] and not belt[i+1] and A[i+1] > 0:
                belt[i], belt[i+1] = False, True
                A[i+1] -= 1
        
        belt[N-1] = False

        if A[0] > 0:
            belt[0] = True
            A[0] -= 1
        
        if A.count(0) >= K:
            break
    return answer

N, K = map(int,sys.stdin.readline().split())
A = deque(list(map(int,sys.stdin.readline().split())))

# response
response = solution(N, K, A)
print(response)
