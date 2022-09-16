import sys
#sys.stdin = open("input.txt","r")
N = int(input())
a = list(map(int,input().split()))
ave = int(sum(a)/N+0.5)#소수 첫째자리에서 반올림함
min = float('inf')
for idx, x in enumerate(a):
    tmp=abs(x-ave)#절대값으로 평균과의 거리를 구해줌
    if tmp < min:
        min = tmp
        score = x
        res = idx+1
    elif tmp == min:
        if x > score:
            score=x
            res=idx+1
print(ave, res)