n = int(input())
liquids = list(map(int,input().split()))
answer_left = 0
answer_right = 0
answer = float('inf')

for i in range(n-1):
    current = liquids[i]
    start = i + 1
    end = n - 1
    
    while start <= end:
        mid = (start + end) // 2
        tmp = current + liquids[mid]
        
        if abs(tmp) < answer:
            answer = abs(tmp)
            answer_left = i
            answer_right = mid
            
            if tmp == 0:
                break
        if tmp < 0:
            start = mid + 1
        else:
            end = mid - 1

print(liquids[answer_left], liquids[answer_right])
