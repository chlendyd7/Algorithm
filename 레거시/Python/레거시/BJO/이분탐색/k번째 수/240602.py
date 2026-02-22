import sys
input = sys.stdin.readline
n = int(input())
k = int(input())

lt, rt = 0, k
answer = 0 
while lt <= rt:
    mid = (lt + rt)//2
    count = 0
    for i in range(1, n+1):
        count += min(mid //i, n)
    
    if count >= k:
        rt = mid - 1
        answer = mid
    else:
        lt = mid + 1

print(answer)