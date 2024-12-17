import sys
input = sys.stdin.readline
n,k = map(int,input().split())
ls=list(map(int,input().split()))
slicing = ls[:k]
maxx = summ = sum(slicing)
for i in range(k,n):
    slicing = ls[i:n-i]
    summ = summ + ls[i] - ls[i-k]
    maxx = max(maxx, summ)

print(maxx)
