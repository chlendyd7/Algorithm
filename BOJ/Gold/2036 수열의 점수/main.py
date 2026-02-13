'''
    한 정수 제거 or 두 정수를 제거
    한 정수를 제거, 그 정수가 점수
    두 정수를 제거 두 정수의 곱이 점수

    점수의 총 합의 최대
'''
def handle_lst(nums, is_positive, has_zero):
    result = 0
    n = len(nums)
    for i in range(0, n-1, 2):
        result += (nums[i] * nums[i+1])
    if n % 2 == 1:
        if is_positive:
            result += nums[-1]
        else:
            if not has_zero:
                result += nums[-1]
    return result


n = int(input())
nums = [int(input()) for _ in range(n)]
min_lst = []
plus_lst = []
result = 0
has_zero = False

for n in nums:
    if n == 1:
        result += 1
    elif n > 1:
        plus_lst.append(n)
    elif n < 0:
        min_lst.append(n)
    else:
        has_zero = True

min_lst.sort()
plus_lst.sort(reverse=True)

result += handle_lst(min_lst, False, has_zero)
result += handle_lst(plus_lst, True, has_zero)
print(result)
