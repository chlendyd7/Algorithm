from collections import Counter

def solution(k, tangerine):
    # dict 형태로 내부 key 값을 계산
    count = Counter(tangerine)
    # sorted = list return
    count_lst = sorted(count.items(), key=lambda x: -x[1])
    answer = 0

    for key, value in count_lst:
        if k <= 0:
            break
        k -= value
        answer += 1
    return answer
