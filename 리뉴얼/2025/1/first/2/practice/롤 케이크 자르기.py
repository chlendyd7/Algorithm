from collections import defaultdict


def solution(topping):
    slicing = 0
    a_dic = defaultdict(int)  # 초기값은 정수형
    for t in topping:
        a_dic[t] += 1
    b_dic = defaultdict(int)
    answer = 0

    for i in range(len(topping)):
        b_dic[topping[i]] += 1
        a_dic[topping[i]] -= 1
        if a_dic[topping[i]] == 0:
            del a_dic[topping[i]]
        if len(a_dic) == len(b_dic):
            answer += 1
        

    
    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))