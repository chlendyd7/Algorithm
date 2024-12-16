# [PCCE 기출문제] 10번 / 공원
# https://school.programmers.co.kr/learn/courses/30/lessons/340198

def solution(mats, park):
    rows = len(park)
    cols = len(park[0])
    max_size = -1

    mats.sort()

    for m in range(len(mats) - 1, -1, -1): # 큰 매트부터 역순으로 조회
        can_place = False

        for i in range(rows - mats[m] + 1): # 매트 배치 가능한 마지막 행 좌표
            for j in range(cols - mats[m] + 1): # 매트 배치 가능한 마지막 열 좌표
                all_minus_one = True

                for x in range(i, i + mats[m]):
                    for y in range(j, j + mats[m]):
                        if park[x][y] != "-1":
                            all_minus_one = False
                            break
                    if not all_minus_one:
                        break

                if all_minus_one: # 모두 빈 공간 "-1" 이라면 배치 가능하다 판단하고 루프 탈출
                    can_place = True
                    break

            if can_place: # 배치 가능하면 탈출
                break

        if can_place: # 배 가능하면 사이즈 저장
            max_size = mats[m]
            break

    return max_size
