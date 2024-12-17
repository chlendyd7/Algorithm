# 라이브러리를 이용한 순열
import itertools as it
n, f = map(int, input().split())
b=[1]*n
cnt = 0
for i in range(1,n):
    b[i]=b[i-1]*(n-i)/i
a=list(range(1,n+1))
for tmp in it.permutations(a): # 모든 순열을 구해줌
    sum=0
    for L, x in enumerate(tmp):
        print(L, x)
    break