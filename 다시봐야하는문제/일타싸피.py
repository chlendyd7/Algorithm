import math

# balls: [ (x,y), (x,y), ... ] 형태, 최대 6개 (흰공 + 5개)
# 예시
balls = [
    (10, 20),   # 내 공 (흰공)
    (30, 40),   # 1번 공 (타겟)
    (-1, -1),   # 2번 공 없음
    (50, 60),   # 3번 공
    (-1, -1),   # 4번 공 없음
    (-1, -1)    # 5번 공 없음
]

# 1. 내 공 좌표
white_ball = balls[0]

# 2. 타겟 공 찾기 (첫 번째 존재하는 공)
target_ball = None
for i in range(1, len(balls)):
    if balls[i][0] != -1 and balls[i][1] != -1:  # -1, -1 이 아닌 경우
        target_ball = balls[i]
        break

if target_ball:
    # 3. 벡터 계산 (타겟공 - 내공)
    dx = target_ball[0] - white_ball[0]
    dy = target_ball[1] - white_ball[1]

    # 4. atan2 로 각도 계산 (라디안)
    radian = math.atan2(dy, dx)

    # 5. degree 변환
    angle = math.degrees(radian)

    # 6. 출력 (power는 100으로 고정)
    power = 100
    print(f"타겟공: {target_ball}, angle: {angle:.2f}°, power: {power}")
else:
    print("타겟 공이 없습니다.")
