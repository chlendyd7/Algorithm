def solution():
    K,N,M = map(int, input().split())
    charges = list(map(int, input().split()))
    now = 0
    cnt = 0
    while now + K < N:
        for i in range(now+K, now, -1):
            if i in charges:
                now = i
                cnt += 1
                break
        else:
            return 0
    return cnt
 
 
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
