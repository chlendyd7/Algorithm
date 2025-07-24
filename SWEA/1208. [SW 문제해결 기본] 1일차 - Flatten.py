def solution():
    dump_cnt = int(input())
    boxs = list(map(int, input().split()))
    for _ in range(dump_cnt):
        boxs.sort()
        boxs[0] += 1
        boxs[-1] -= 1
    
    boxs.sort()
    return boxs[-1] - boxs[0]


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')