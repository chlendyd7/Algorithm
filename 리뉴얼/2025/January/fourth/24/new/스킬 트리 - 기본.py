def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_order = list(skill)

        for s in skill_tree:
            if s in skill_order:
                if s != skill_order.pop(0):
                    break
        else:
            answer += 1
    return answer
