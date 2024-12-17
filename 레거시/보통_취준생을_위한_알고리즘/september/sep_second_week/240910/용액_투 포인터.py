n = int(input())
liquids = list(map(int,input().split()))

left = 0
right = n-1

answer = abs(liquids[left] + liquids[right])
answer_left = left
answer_right = right

while left < right:
    mid = liquids[left] + liquids[right]

    if abs(mid) < answer:
        answer_left = left
        answer_right = right
        answer = abs(mid)

        if answer == 0:
            break
    
    if mid < 0:
        left += 1
    else:
        right -= 1

print(liquids[answer_left], liquids[answer_right])
