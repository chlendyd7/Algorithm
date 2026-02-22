n,s = map(int, (input().split()))
nums = list(map(int,input().split()))

left, right = 0, 0
num_sum = 0
min_length = 1e9

while True:
    if num_sum >= s:
        min_length = min(min_length, right-left)
        num_sum -= nums[left]
        left += 1
    elif right == n:
        break
    else:
        num_sum += nums[right]
        right+=1

if min_length == 1e9:
    print(0)
else:
    print(min_length)
