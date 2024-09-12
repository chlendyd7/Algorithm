n = int(input())
liquid = list(map(int,input().split()))
left, right = 0, n-1
answer = float('inf')
a_left, a_right = 0, n-1
while left < right:
    mid = liquid[left] + liquid[right]
    if abs(mid) < answer:
        a_left = left
        a_right = right
        answer = abs(mid)

        if answer == 0:
            break
    if mid < 0:
        left += 1
    else:
        right -=1

print(liquid[a_left], liquid[a_right])