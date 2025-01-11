from collections import deque


def solution(a):
    answer = 2
    n = len(a)
    
    left_min = [0] * n
    right_min = [0] * n
    
    left_min[0] = a[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], a[i])
    
    right_min[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i + 1], a[i])
    
    count = 0
    for i in range(n):
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            count += 1
    return count
