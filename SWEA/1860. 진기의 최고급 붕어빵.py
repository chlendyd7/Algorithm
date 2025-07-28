'''
- N명의 손님
- M초의 시간이 지나면 K개의 붕어빵을 만들 수 있다
'''
from collections import deque


def solution():
    N, M, K = map(int,input().split())
    arrived = list(map(int, input().split()))
    bongbread = []
    arrived.sort()
    arrived = deque(arrived)
    
    if arrived[0] == 0:
        return "Impossible"
    
    bongbread = 0
    for i in range(1, arrived[-1] + 1):
        if i % M == 0:
            bongbread += K

        while arrived and arrived[0] == i:
            if bongbread > 0:
                bongbread -= 1
                arrived.popleft()
            else:
                return "Impossible"

    return "Possible"



T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')


T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())  # N:인원, M:시간, K:개수
    sec = list(map(int, input().split()))
    sec.sort()
    time = M
 
    ans = "Possible"
    while len(sec) > 0:
        if time > min(sec):
            ans = "Impossible"
            break
        else:
            if K > len(sec):
                K = len(sec)
            del sec[:K]
            time += M
 
    print(f"#{test_case} {ans}")
