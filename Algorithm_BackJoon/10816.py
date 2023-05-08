import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int,input().split()))
d = {} #시간 제한을 해결하기 위한 dictionary

for i in ls:
    if i not in d: #ls의 값이 dict에 처음 넣는 값이라면
        d[i] = 1
    else: #계속해서 +1로 value를 증가
        d[i] = d[i]+1

m = int(input())
ls2 = list(map(int,input().split()))

for j in ls2:
    if j in d:
        print(d[j], end=' ')
    else:
        print(0, end=' ')
    