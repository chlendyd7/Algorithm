from itertools import permutations



def is_match(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i] != len(banned_id[i])):
            return False
        for j in range(len(users[i])):
            if banned_id[i][j] == '*':
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id)))
    ban_set = []

    for user in user_permutation:
        if is_match(user, banned_id):
            users = set(users)
            if users not in ban_set:
                ban_set.append(users)