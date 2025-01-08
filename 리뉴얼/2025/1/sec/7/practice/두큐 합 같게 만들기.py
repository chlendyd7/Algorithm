from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum_q1, sum_q2 = sum(q1) , sum(q2)
    total_sum = sum_q1 + sum_q2

    if total_sum % 2 != 0:
        return -1
    
    target = total_sum // 2
    max_move = len(q1) + len(q2) * 2
    count = 0

    while count <= max_move:
        if sum_q1 == sum_q2:
            return count
        elif sum_q1 > target:
            val = q1.popleft()
            sum_q1 -= val
            q2.append(val)
        else:
            val = q2.popleft()
            sum_q2 -= val
            q1.append(val)
            sum_q1 += val
    
        count += 1

    return -1