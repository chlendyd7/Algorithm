from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum_q1, sum_q2 = sum(q1), sum(q2)
    total_sum = sum_q1 + sum_q2
    
    if total_sum % 2 != 0:
        return -1

    target = total_sum // 2
    max_move = len(q1) + len(q2)