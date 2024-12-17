def check(x):
    now = -1
    cnt = 0
    for i in range(k):
        if now <= nums[i]:
            cnt += 1
            now = nums[i] + x
    return cnt >= m

n,m,k = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
end = nums[-1]
while start + 1 < end:
    mid = (start + end) // 2
    if check(mid):
        start = mid
    else:
        end = mid

ans = []
now = 0
cnt = 0
for i in range(k):
    if now <= nums[i] and cnt < m:
        ans.append('1')
        now = nums[i] + start
        cnt += 1
    else:
        ans.append('0')

print(''.join(ans))
