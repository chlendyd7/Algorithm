def solution(scores):
    target_a, target_b = scores[0]
    target_cnt = target_a + target_b
    maxb = 0
    answer = 0
    scores = sorted(scores, key=lambda x:(-x[0], x[1]))
    
    for score in scores:
        a,b = score
        if target_a < a and target_b < b:
            return -1
        if b >= maxb:
            maxb = b
            if a + b > target_cnt:
                answer += 1
    return answer + 1