from collections import deque
import sys

def simulateConveyorBelt(belt_length, max_zero_durability, durability_list):
    step_count = 0  # 단계 수를 기록
    robot_belt = deque([False] * belt_length)  # 로봇이 위치하는 벨트 (각 칸에 로봇이 있는지 여부)
    
    while True:
        step_count += 1

        # 1. 벨트 회전
        durability_list.rotate(1)
        robot_belt.rotate(1)
        
        # 회전 후 로봇이 내리는 위치에 있는지 확인
        robot_belt[belt_length - 1] = False

        # 2. 로봇 이동 (뒤에서부터 이동)
        for i in range(belt_length - 2, -1, -1):
            if robot_belt[i] and not robot_belt[i + 1] and durability_list[i + 1] > 0:
                robot_belt[i], robot_belt[i + 1] = False, True
                durability_list[i + 1] -= 1

        # 로봇이 내리는 위치에 있으면 내려줌
        robot_belt[belt_length - 1] = False

        # 3. 새로운 로봇을 올림
        if durability_list[0] > 0:
            robot_belt[0] = True
            durability_list[0] -= 1

        # 4. 내구도가 0인 칸의 개수가 max_zero_durability 이상일 때 종료
        if durability_list.count(0) >= max_zero_durability:
            break

    return step_count

# 입력 받기
belt_length, max_zero_durability = map(int, sys.stdin.readline().split())
durability_list = deque(list(map(int, sys.stdin.readline().split())))

# 결과 출력
result = simulateConveyorBelt(belt_length, max_zero_durability, durability_list)
print(result)
