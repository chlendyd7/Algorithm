import sys
input = sys.stdin.readline

n = int(input())
ls = set(map(int,input().split()))

m = int(input())
ls2 = list(map(int,input().split()))

for i in range(m):
    if ls2[i] in ls:
        print(1, end=' ')
    else:
        print(0, end=' ')