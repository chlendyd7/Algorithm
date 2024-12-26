def solution(k, d):
    answer = 0
    radius = d // k  # 정수로 반지름을 변환

    for n in range(radius + 1):
        # m의 최대값을 계산
        max_m = int((radius**2 - n**2) ** 0.5)
        answer += (max_m + 1)  # 가능한 m의 개수

    return answer
