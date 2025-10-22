import sys
input = sys.stdin.readline
n,c = map(int,input().split())
ls = [int(input().rstrip()) for _ in range(n)]
ls.sort()
lt, rt = 1, ls[-1] - ls[0]
result = 0 

while lt<=rt:
    mid = (lt + rt) // 2
    
    now = 0
    count = 1
    for i in range(len(ls)):
        if ls[i] - ls[now] >= mid:
            now = i
            count += 1
    if count >= c:
        lt = mid + 1
        result = mid
    else:
        rt = mid - 1

print(result)
