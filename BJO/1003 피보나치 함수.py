T = int(input())
nums = [int(input()) for _ in range(T)]
max_n = max(nums)

dp = [0] * 41

cnt0 = [0] * (max_n + 1)
cnt1 = [0] * (max_n + 1)
cnt0[0] = 1
cnt1[0] = 0
cnt0[1] = 0
cnt1[1] = 1

for i in range(2, max_n+1):
    cnt0[i] = cnt0[i-1] + cnt0[i-2]
    cnt1[i] = cnt1[i-1] + cnt1[i-2]
for num in nums:
    print(cnt0[num], cnt1[num])
