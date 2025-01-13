from itertools import permutations

def is_match(banned_id, user_id):
    # banned_id와 user_id의 길이가 다르면 매칭 불가
    if len(banned_id) != len(user_id):
        return False
    
    # banned_id의 각 문자와 user_id 비교
    for b_char, u_char in zip(banned_id, user_id):
        if b_char != '*' and b_char != u_char:
            return False
    
    return True

def solution(user_id, banned_id):

    # 가능한 모든 조합 생성
    banned_permutations = list(permutations(user_id, len(banned_id)))
    print(banned_permutations)
    valid_combinations = set()
    
    for perm in banned_permutations:
        match = True
        for b_id, u_id in zip(banned_id, perm):
            if not is_match(b_id, u_id):
                match = False
                break
        if match:
            valid_combinations.add(tuple(sorted(perm)))
    
    return len(valid_combinations)
