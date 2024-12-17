n,s = map(int,input().split())
nums = list(map(int,input().split()))

answer = 1e9
count = 0
left, right = 0,0
while True:
    if count >= s:
        answer = min(answer, right-left)
        count -= nums[left]
        left += 1
    elif right == n:
        break
    else:
        count += nums[right]
        right += 1

if answer == 1e9:
    print(0)
else:
    print(answer)
