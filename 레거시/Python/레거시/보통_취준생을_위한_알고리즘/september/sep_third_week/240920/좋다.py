n = int(input())
num_lst = list(map(int, input().split()))

answer = 0
num_lst.sort()

for i in range(n):
    now = num_lst[i]
    left = 0
    right = n - 1
    
    while left < right:
        if left == i:  # left가 i와 같으면 건너뜀
            left += 1
            continue
        if right == i:  # right가 i와 같으면 건너뜀
            right -= 1
            continue
        
        tmp = num_lst[left] + num_lst[right]
        
        if tmp == now:
            answer += 1
            break
        elif tmp < now:
            left += 1
        else:
            right -= 1

print(answer)
