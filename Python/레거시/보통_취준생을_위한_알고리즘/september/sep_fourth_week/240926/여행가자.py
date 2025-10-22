from collections import deque


def solution(start, end):
    q = deque()
    


n = int(input())
m = int(input())
graph = [list(map(bool, input().split())) for _ in range(n)]
target = list(map(int,input().split()))

answer = True
for i in range(m-1):
    if not solution(target[i], target[i+1]):
        answer = False
        break

if answer:
    print('YES')
else:
    print('NO')