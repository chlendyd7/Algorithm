import sys
input = sys.stdin.readline

n = int(input())
ls = set(map(int,input().split()))
# 시간제한으로 인한 set
m = int(input())
ls2 = list(map(int,input().split()))

for i in range(m):
    if ls2[i] in ls: #ls2[i] 번째가 ls2 안에 존재한다면
        print(1, end=' ')
    else:
        print(0, end=' ')