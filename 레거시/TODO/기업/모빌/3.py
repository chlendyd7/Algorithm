def solution(D, T):

    def check(i):
        if 'P' in T[i]:
            exist[0] = i
            time[0] += T[i].count('P')
        if 'G' in T[i]:
            exist[1] = i
            time[1] += T[i].count('G')
        if 'M' in T[i]:
            exist[2] = i
            time[2] += T[i].count('M')

    dis = [0] * len(D)
    dis[0] = D[0]
    exist = [0] * 3
    time = [0] * 3
    check(0)
    # 거리 누적합 계산
    for i in range(1, len(D)):
        dis[i] = D[i] + dis[i-1]
        check(i)
        # T에서 각 문자 'P', 'G', 'M'에 대해 처리
        
    
    answer = 0
    # 최대 값을 찾기
    for k in range(3):
        answer = max(answer, dis[exist[k]] * 2 + time[k])
    
    return answer

# 예시 테스트
D = [2, 5] 
T = ['PGP', 'M']
print(solution(D, T))  # 결과 값 출력