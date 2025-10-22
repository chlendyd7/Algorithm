import sys
input = sys.stdin.readline
n,m = map(int,input().split())
ls = list(map(int,input().split()))
ls.insert(0,0)
plus_ls = [0] * (n+1)

plus = 0 
for i in range(1, n+1):
    plus += ls[i]
    plus_ls[i] = plus

for x in range(m):
    i,j = map(int,input().split())
    print(plus_ls[j] - plus_ls[i-1])
