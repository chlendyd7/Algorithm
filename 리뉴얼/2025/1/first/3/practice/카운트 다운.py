def solution(target):
    p = {}
    for i in range(1, 21):
        p[2 * i] = 0
        p[3 * i] = 0
    for i in range(1, 21):
        p[i] = 1
    p[50] = 1
    answer = []

    # min_darts[i] 는 i를 만드는 최선의 다트 수 (최소한의 다트 수)
    min_darts = [100001] * 100001
    # max_sbs[i]는 i를 만드는 최선의 조합 중에서 최대의 싱글or불 수
    max_sbs = [0] * 100001

    return answer