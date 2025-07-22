def solution():
    lst = list(map(int, input().split()))
    lst.sort()
    return round(sum(lst[1:len(lst)-1]) / (len(lst) - 2))


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')


# T = int(input())
# for tc in range(1,T+1) :
#     seq = list(map(int,input().split()))
#     seq.sort()
#     ret = sum(seq[1:-1]) / 8
#     print(f'#{tc} {ret:1.0f}')
