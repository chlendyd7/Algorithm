from collections import defaultdict

def solution(weights):
    answer = 0
    length = len(weights)
    weight_dict = defaultdict(int)
    
    for weight in weights :
        weight_dict[weight] += 1
    
    for key, val in weight_dict.items() :
        if val > 1 :
            answer += val * ( val - 1) // 2
        if key*2 in weight_dict :
            answer += val * weight_dict[key*2]
        if key*3 % 2 == 0 and key*3 // 2 in weight_dict :
            answer += val * weight_dict[key*3 // 2]
        if key*4 % 3 == 0 and key*4 // 3 in weight_dict :
            answer += val * weight_dict[key*4 // 3]

    return answer
 
# 출처: https://magentino.tistory.com/53 [마젠티노's:티스토리]