def solution(routes):
    # 구간 정렬: 종료 지점 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    
    camera_count = 0
    last_camera = -30001  # 카메라 설치 위치 초기화

    for start, end in routes:
        # 현재 구간의 시작 지점이 마지막 카메라 위치보다 크면 새로운 카메라 설치
        if start > last_camera:
            camera_count += 1
            last_camera = end  # 현재 구간의 종료 지점에 카메라 설치

    return camera_count

# 예시 사용
routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
print(solution(routes))  # 출력: 2
