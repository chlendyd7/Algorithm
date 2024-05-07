import sys
input = sys.stdin.readline
n,k = map(int,input().split())
ls=list(map(int,input().split()))
summ = maxx = sum(ls[:k])
for i in range(k,n):
    summ = summ + ls[i] - ls[i-k]
    maxx = max(maxx, summ)
print(maxx)