from itertools import combinations

N = int(input())
nums = []

for i in range(1, 11):  # 1자리부터 10자리까지
    for comb in combinations(range(10), i):
        num = int(''.join(map(str, sorted(comb, reverse=True))))
        nums.append(num)

nums.sort()

if N < len(nums):
    print(nums[N])
else:
    print(-1)
