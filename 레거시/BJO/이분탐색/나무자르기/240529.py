import sys
input = sys.stdin.readline
n,m = map(int,input().split())
ls = list(map(int,input().split()))

lt, rt = 0, max(ls)
while lt<=rt:
    mid = (lt + rt) // 2
    trees = 0
    for i in ls:
        if i >= mid:
            trees += i-mid
    
    if trees >= m:
        lt = mid + 1
    else:
        rt = mid - 1

print(rt)