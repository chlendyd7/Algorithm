from collections import defaultdict


def solution(keymap, targets):
    key_dict = {}

    for key in keymap:
        for i in range(len(key)):
            if key[i] in key_dict:
                key_dict[key[i]] = min(key_dict[key[i]], i+1)
            else:
                key_dict[key[i]] = i + 1
    
    answer = []
    # 아래 부분 한번 더 보기
    for target in targets:
        total_time = 0
        for char in target:
            if char in key_dict:
                total_time += key_dict[char]
            else:
                total_time = -1
                break
        
        answer.append(total_time)

    return answer