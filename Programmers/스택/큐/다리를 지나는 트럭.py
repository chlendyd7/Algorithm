'''
2	10	[7,4,5,6]	8

시뮬레이션?

'''
from collections import deque
def solution(bridge_length, weight, truck_weights):
    q = deque([0]* bridge_length)
    answer = 0
    truck_index = 0
    bridge_weight = 0

    while truck_index < len(truck_weights):
        bridge_weight -= q.popleft()
        answer += 1

        if bridge_weight + truck_weights[truck_index] <= weight:
            q.append(truck_weights[truck_index])
            bridge_weight += truck_weights[truck_index]
            truck_index += 1
        else:
            q.append(0)
        
        print(answer)

    answer += bridge_length

    return answer

print(solution(2,10,[7,4,5,6]))