import sys
input = sys.stdin.readline
n,c = map(int,input().split())
ls = [int(input()) for _ in range(n)]
ls.sort()
lt, rt = 1, ls[-1] - ls[0]
result = 0

while lt <= rt:
    mid = (lt + rt) // 2
    
    now = ls[0]
    count = 1
    for i in range(len(ls)):
        if ls[i] >= now + mid:
            count += 1
            now = ls[i]
    
    if count >= c:
        lt = mid + 1
    else:
        rt = mid - 1

print(rt)