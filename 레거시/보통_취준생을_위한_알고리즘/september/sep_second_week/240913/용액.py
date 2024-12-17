n = int(input())
liquied = list(map(int,input().split()))

left, right = 0,n-1
a_left, a_right = 0,right
answer = float('inf')
while left < right:
    mid = liquied[left] + liquied[right]
    if abs(mid) < answer:
        a_left = liquied[left]
        a_right = liquied[right]
        answer = abs(mid)
        if answer == 0:
            break

    if mid < 0:
        left += 1
    else:
        right -= 1

print(a_left, a_right)
