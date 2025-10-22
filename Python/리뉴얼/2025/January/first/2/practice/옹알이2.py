def solution(babbling):
    crying = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for b in babbling:
        for c in crying:
            if c*2 not in b:
                b = b.replace(c, ' ')
        if b.isspace():
            cnt += 1
    return cnt