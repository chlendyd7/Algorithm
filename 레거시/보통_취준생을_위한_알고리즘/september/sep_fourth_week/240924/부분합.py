n, s = map(int, input().split())
nums = list(map(int,input().split()))

left, right = 0,0
answer = 1e9
num_sum = 0

while True:
    if num_sum >= s:
        print(num_sum)
        answer = min(answer, right-left)
        num_sum -= nums[left]
        left += 1
    elif right == n:
        break
    else:
        num_sum += nums[right]
        right += 1

print(answer)
