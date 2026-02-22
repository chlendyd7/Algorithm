n,m,k = map(int, input().split())
position = list(map(int, input().split()))

def check(x):
    now = -1
    cnt = 0
    for i in range(k):
        if now <= position[i]:
            cnt += 1
            now = position[i] + x
    return cnt >= m


start = 0
end = position[-1] + 1
while start <= end:
    mid = (start + end) // 2
    if check(mid):
        start = mid
    else:
        end = mid

ans = []
now = 0 
cnt = 0
for i in range(k):
    if now <= position[i] and cnt < m:
        ans.append('1')
        now = position[i] + start
        cnt += 1
    else:
        ans.append('0')

print(''.join(ans))