n = int(input())
nums = list(map(int,input().split()))
visited = [0] * 100001

left = 0
right = 0
answer = 0
while left <= right and right < n:
    if visited[nums[right]] == 0:
        visited[nums[right]] = 1
        right += 1
        answer += (right - left)
    else:
        while visited[nums[right]]:
            visited[nums[left]] = 0
            left += 1
print(answer)
