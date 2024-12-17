def okensu(n, nums):
    result = [-1] * n  # 결과를 -1로 초기화
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i) #for 문을 통해 index를 구현
    
    return result

# 입력
n = int(input())
nums = list(map(int, input().split()))

# 결과 출력
print(" ".join(map(str, okensu(n, nums))))
