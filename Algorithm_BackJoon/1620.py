import sys
input = sys.stdin.readline
n, m = map(int,input().split())
ls = {}

for i in range(n):
    name = input().strip()
    ls[name] = i+1

ls_reverse = dict(map(reversed, ls.items()))
check = [input().strip() for m in range(m)]




for i in check:
    if i in ls:
        print(ls[i])
    else:
       print(ls_reverse[int(i)])
