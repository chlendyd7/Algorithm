def solution(scores: list):
    target_a, target_b = scores[0]
    count = target_a + target_b
    scores.sort(key=lambda x: (-x[0], x[1]))
    maxb = 0
    answer = 0
    for a,b in scores:
        if a > target_a and b > target_b:
            return -1
        if b >= maxb:
            maxb = b
            if a + b > count:
                answer += 1

    return answer