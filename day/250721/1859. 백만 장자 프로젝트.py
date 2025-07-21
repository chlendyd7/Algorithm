def solution():
    n = int(input())
    nums = list(map(int, input().split()))
    
    max_num = 0
    result = 0
    for num in reversed(nums):
        if num > max_num:
            max_num = num
        else:
            result += (max_num - num)

    return result

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
