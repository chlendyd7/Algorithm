n = int(input())
lst = list(map(int,input().split()))
left, right = 0,0
answer = 0
visited = [False] * 100001
while left <= right and right < n:
    if not visited[lst[right]]:
        visited[lst[right]] = True
        right += 1
        answer += right - left
    else:
        while visited[lst[right]]:
            visited[lst[left]] = False
            left += 1
print(answer)
