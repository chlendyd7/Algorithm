from collections import defaultdict


def solution(skill, skill_trees):
    parent = {
        skill[i]: skill[i-1] for i in range(1, len(skill))
    }
    answer = 0

    for skill_tree in skill_trees:
        learn = set()
        is_valid = True

        for s in skill_tree:
            if s in parent:
                if parent[s] not in learn:
                    is_valid = False
                    break
            learn.add(s)
        if is_valid:
            answer += 1
    return answer



    answer = -1
    return answer