from collections import deque

def solution(queue1, queue2):
    # 두 큐를 deque로 변환
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    # 초기 상태
    sum_q1, sum_q2 = sum(q1), sum(q2)
    total_sum = sum_q1 + sum_q2
    
    # 총합이 홀수면 답 불가능
    if total_sum % 2 != 0:
        return -1
    
    target = total_sum // 2
    max_moves = len(q1) + len(q2) * 2  # 최대 이동 가능 횟수
    count = 0
    
    # 투 포인터 방식으로 합 조정
    while count <= max_moves:
        if sum_q1 == target:  # 두 큐의 합이 같아졌다면 종료
            return count
        elif sum_q1 > target:  # q1의 합이 더 크면 q1에서 원소 이동
            val = q1.popleft()
            sum_q1 -= val
            q2.append(val)
        else:  # q2의 합이 더 크면 q2에서 원소 이동
            val = q2.popleft()
            sum_q2 -= val
            q1.append(val)
            sum_q1 += val
        
        count += 1
    
    return -1  # 최대 이동 횟수를 초과한 경우
