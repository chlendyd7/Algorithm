def solution(picks, minerals):
    def scan_minerals(minerals):
        i = 0
        flag = True
        counted = []
        while flag:
            target = []
            if i + 5 < len(minerals):
                target = minerals[i:i+5]
                i += 5
            else:
                target = minerals[i:]
                flag = False
            
            dias, irons, stones = target.count('diamond'), target.count('iron'), target.count('stone')
            counted.append([dias, irons, stones])
        
        counted.sort(key=lambda x: (-x[0], -x[1]))
        return counted

    def calculate(picks, minerals):
        result = 0
        for target in minerals:
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

    if sum(picks) * 5 < len(minerals):
        minerals = minerals[:sum(picks) * 5]
    scan_mineral = scan_minerals(minerals)
    answer = calculate(picks, scan_mineral)

    return answer