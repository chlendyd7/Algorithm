import sys
input = sys.stdin.readline
k,n = map(int,input().split())
list = [int(input()) for _ in range(k)]

start, end = 0, max(list)

while start<= end:
    mid = (start+end) // 2
    lines = 0 
    for ls in list:
        lines += ls // mid
    
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
