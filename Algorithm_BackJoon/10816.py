import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int,input().split()))
d = {}

for i in ls:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i]+1

m = int(input())
ls2 = list(map(int,input().split()))

for j in ls2:
    if j in d:
        print(d[j], end=' ')
    else:
        print(0, end=' ')
    