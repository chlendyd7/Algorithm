def solution(k, m, score):
    sort_score = sorted(score, reverse=True)
    temp_stack = []
    answer = 0
    for i in range(len(score)):
        temp_stack.append(sort_score[i])
        if len(temp_stack) == m:
            answer += min(temp_stack) * m
            temp_stack = []
    return answer
