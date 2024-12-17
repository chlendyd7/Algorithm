n,c = map(int,input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()
left = 1
right = nums[-1] - nums[0]
answer = 0

while left <= right:
    mid = (left + right) // 2
    now = 0
    cnt = 1
    for i in range(n):
        if nums[i] - nums[now] >= mid:
            cnt += 1
            now = i
    
    if cnt >= c:
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)
