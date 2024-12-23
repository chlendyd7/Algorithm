from collections import deque

def solution(x, y, n):
    if x == y:  # 시작과 목표가 같으면 바로 반환
        return 0

    queue = deque([(x, 0)])  # (현재 값, 연산 횟수)
    visited = set([x])  # 시작 값 방문 처리

    while queue:
        current, steps = queue.popleft()

        for next_val in (current + n, current * 2, current * 3):
            if next_val == y:  # 목표에 도달하면 연산 횟수 반환
                return steps + 1
            if next_val < y and next_val not in visited:
                visited.add(next_val)
                queue.append((next_val, steps + 1))
    
    return -1  # 목표에 도달하지 못한 경우