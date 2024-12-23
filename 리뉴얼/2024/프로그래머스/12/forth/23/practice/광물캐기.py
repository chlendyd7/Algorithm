    
def scan_mierals(minerals):
    i = 0
    flag = True
    counted = []
    while flag:
        target = []
        if i + 5 < len(minerals):
            target = minerals[i:i+5]
        else:
            target = minerals[i:]
            flag = False
        dias, irons, stones = target.count('diamond'), target.count('iron'), target.count('stone')
        counted.append([dias, irons, stones])
        i += 5
    counted.sort(key=lambda x: (-x[0], -x[1]))
    return counted

def calculate(counted, picks):
    result = 0
    for target in counted:
        if picks[0] > 0:
            picks[0] -= 1
            result += sum(target)
        elif picks[1] > 0:
            picks[1] -= 1
            result += target[0] * 5 + target[1] + target[2]
        elif picks[2] > 0:
            picks[2] -= 1
            result += target[0] * 25 + target[1] * 5 + target[2]
        else:
            break
    return result

def solution(picks, minerals):
    if sum(picks) * 5 < len(minerals):
        minerals = minerals[:sum(picks) * 5]
    counted = scan_mierals(minerals)
    answer = calculate(counted, picks)
    return answer

print(solution([1, 3, 2],	["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))