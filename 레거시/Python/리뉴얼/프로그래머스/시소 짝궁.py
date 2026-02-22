from collections import defaultdict


def solutions(weights):
    weights_dict = defaultdict(int)
    answer = 0

    for w in weights:
        weights_dict[w] += 1
    
    for key, val in weights_dict.items():
        if val > 1:
            answer += val * (val - 1) // 2
        if key * 2 in weights_dict:
            answer += val * weights_dict[key*2]
        if key * 3 % 2 == 0 and key * 3 // 2 in weights_dict:
            answer += val * weights_dict[key*3 / 2]
        