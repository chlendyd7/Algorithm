def solution(scores):
    target_a, target_b = scores[0]
    target = target_a + target_b
    sort_score = sorted(scores, key=lambda x:(-x[0], x[1]))
    answer = 0
    maxb = 0

    for s in sort_score:
        now_a, now_b = s
        if target_a < now_a and target_b < now_b:
            return -1
        if now_b >= maxb:
            maxb = now_b
            if now_a+now_b > target:
                answer += 1
        

    return answer + 1
