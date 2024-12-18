def solution(keymap, targets):
    key_dict = dict()
    answer = []
    for key in keymap:
        for i in range(len(key)):
            if key_dict[key[i]] in key[i]:
                key_dict[key[i]] = min(key_dict[key[i]], i+1)
            else:
                key_dict[key[i]] = i + 1
    
    for target in targets:
        cnt = 0
        for t in target:
            if key_dict in t:
                cnt += key_dict[t]
            else:
                cnt = -1
                break
        answer.append(cnt)

    return answer


def solution(keymap, targets):
    # 각 문자의 최소 눌러야 할 횟수를 기록할 딕셔너리
    key_dict = {}
    
    # keymap을 한 번 순회하여 각 문자의 최소 횟수 계산
    for key in keymap:
        for i, char in enumerate(key):
            if char not in key_dict:  # 문자가 딕셔너리에 없으면
                key_dict[char] = i + 1  # 키의 인덱스 + 1을 저장 (1부터 시작)
            else:
                key_dict[char] = min(key_dict[char], i + 1)  # 최소값 갱신
    
    answer = []
    
    # target 문자열에 대해 각 문자를 입력하는 최소 횟수 계산
    for word in targets:
        total_time = 0  # 전체 키 횟수
        for char in word:
            if char in key_dict:  # 문자가 keymap에 있으면
                total_time += key_dict[char]
            else:  # 문자가 keymap에 없으면
                total_time = -1
                break
        
        answer.append(total_time)
    
    return answer
