from collections import deque

def solution():
    _ = input()
    nums = list(map(int, input().split()))
    min_num = min(nums)
    reduce_cycle = (min_num // 15) * 15
    nums = [num - reduce_cycle + 15 for num in nums]
    
    q = deque(nums)
    
    decrease = 1
    while True:
        num = q.popleft() - decrease
        if num <= 0:
            q.append(0)
            break
        q.append(num)
        
        decrease += 1
        if decrease > 5:
            decrease = 1
    
    return list(q)

for t in range(1, 11):
    result = solution()
    print(f'#{t}', ' '.join(map(str, result)))
