def solution(babbling):
    cring = ["aya", "ye", "woo", "ma"]
    answer = 0
    for baby in babbling:
        for c in cring:
            if c * 2 not in baby:
                baby = baby.replace(c, ' ')
        
        if baby.isspace():
            answer += 1
    return answer
