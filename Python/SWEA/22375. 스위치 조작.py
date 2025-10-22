def solution():
    N = int(input())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    cnt = 0
    for idx in range(N):        
        if Ai[idx] != Bi[idx]:
            for i in range(idx, N):
                if Ai[i]:
                    Ai[i] = 0
                else:
                    Ai[i] = 1

            cnt += 1
            idx += 1
    return cnt


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
