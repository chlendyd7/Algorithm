from collections import defaultdict

def make_nums_count(k, nums):
    prefix_sum = 0
    dic = defaultdict(int)
    cnt = 0
    
    dic[0] = 1
    
    for num in nums:
        prefix_sum += num
        
        if prefix_sum - k in dic:
            cnt += dic[prefix_sum - k]

        dic[prefix_sum] += 1
    
    return cnt
    
    

n,k = map(int,input().split())

nums = list(map(int,input().split()))
print(make_nums_count(k, nums))

