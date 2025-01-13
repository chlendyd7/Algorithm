from itertools import permutations

def is_match(banned_id, user_id):
    if len(banned_id) != len(user_id):
        return False
    
    for b_char, u_char in zip(banned_id):
        if b_char != '*' and b_char != u_char:
            return False
    return True

def solution(user_id, banned_id):
    banned_permutations = list(permutations(user_id, len(banned_id)))
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
