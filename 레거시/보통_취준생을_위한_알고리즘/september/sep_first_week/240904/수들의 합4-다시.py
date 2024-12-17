from collections import defaultdict

def count_subarrays_with_sum_k(n, k, arr):
    prefix_sum = 0
    count = 0
    prefix_sum_map = defaultdict(int)
    
    # 처음부터 합이 K인 경우를 고려해 0을 한 번 카운트
    prefix_sum_map[0] = 1
    
    for num in arr:
        prefix_sum += num
        
        # (prefix_sum - K) 가 이전에 나타난 적이 있으면 그것과 현재 위치 사이의 구간합이 K가 됨
        if prefix_sum - k in prefix_sum_map:
            count += prefix_sum_map[prefix_sum - k]
        
        # 현재의 prefix_sum 값을 맵에 저장
        prefix_sum_map[prefix_sum] += 1
    
    return count

# 입력 받기
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 결과 출력
print(count_subarrays_with_sum_k(n, k, arr))
