import sys
input = sys.stdin.readline
n,m = map(int,input().split())
ls = list(map(int,input().split()))
plus_list = [0]
temp = 0

for i in ls:
    temp += i
    plus_list.append(temp)

for _ in range(n):
    i,j = map(int,input().split())
    print(plus_list[j]-plus_list[i-1])
