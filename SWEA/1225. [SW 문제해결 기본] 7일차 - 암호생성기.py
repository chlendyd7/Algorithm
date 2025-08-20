from collections import deque

def solution():
    _ = input()
    nums = list(map(int, input().split()))
    
    # 모든 수가 한 자리 수가 될 때까지 15로 나누기
    while True:
        all_single_digit = True
        for num in nums:
            if num >= 10:
                all_single_digit = False
                break
        
        if all_single_digit:
            break
        
        for i in range(8):
            nums[i] //= 15
    
    nums = deque(nums)
    
    # 1,2,3,4,5를 차례로 빼는 사이클 반복
    while True:
        for decrease in range(1, 6):
            if not nums:
                break
                
            num = nums.popleft()
            num -= decrease
            
            # 0 이하가 되면 0으로 설정하고 종료
            if num <= 0:
                num = 0
                nums.append(num)
                return list(nums)
            
            nums.append(num)

for t in range(1, 11):
    result = solution()
    print(f'#{t}', ' '.join(map(str, result)))
