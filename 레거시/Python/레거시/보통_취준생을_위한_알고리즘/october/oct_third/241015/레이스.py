n,m,k = map(int, input().split())
position = list(map(int, input().split()))

def check(x):
    now = -1
    cnt = 0
    for i in range(k):
        if now <= position[i]:
            cnt += 1
            now = position[i] + x
    
    if cnt < m:
        return False
    return True

start = 0
end = position[-1] + 1
while start <= end:
    mid = (start + end) // 2
    if check(mid):
        start = mid
    else:
        end = mid - 1
ans = ''
now = 0
cnt = 0
for i in range(k):
    if now <= position[i] and cnt < m:
        ans += '1'
        now = position[i] + start