def solution(target):
    # 다트 하나를 던졌을 때 나올 수 있는 모든 점수에 대해서,
		# 싱글/불로 만들 수 있으면 1, 없으면 0을 반환하는 딕셔너리 P
		# 를 고려한다.
    P = {}  # {score: sb} 점수, single or bull 인지
    for i in range(1, 21):
        P[2 * i] = 0
        P[3 * i] = 0
		# <최선의 상황만 고려>
		# 싱글/불로 만들 수 있는 점수는 항상 싱글/불로 만든다고 가정한다.
    for i in range(1, 21): # Single일 때를 1로 덮어씌운다.
        P[i] = 1
    P[50] = 1 # bull일 때를 1로 덮어씌운다.
    
    # min_darts[i] 는 i를 만드는 최선의 다트 수 (최소한의 다트 수)
    min_darts = [100001] * 100001
    # max_sbs[i]는 i를 만드는 최선의 조합 중에서 최대의 싱글or불 수
    max_sbs = [0] * 100001
		
		# 다트 딱 하나를 던져서 만들 수 있는 점수라면,
		# min_darts[i] 는 1이고, 싱글/불 여부는 미리 만들어 놓은 P에서 얻어오면 된다.
    for i, sb in P.items():
        min_darts[i] = 1
        max_sbs[i] = sb

    for t in range(1, target + 1):
        if min_darts[t] != 100001:
            continue
            
        mn, sb = 100001, 0
        for score, _sb in P.items():
            if t - score < 0:
                continue
                
            s = t - score
            if (min_darts[s] + 1 < mn) or (min_darts[s] + 1 == mn and max_sbs[s] + _sb > sb):
                mn = min_darts[s] + 1
                sb = max_sbs[s] + _sb

        min_darts[t] = mn
        max_sbs[t] = sb

    return [min_darts[target], max_sbs[target]]