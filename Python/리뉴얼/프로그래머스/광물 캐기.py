def solution(picks, minerals):
    def scan_minerals(minerals):
        i = 0
        counted = []
        while i < len(minerals):
            target = minerals[i:i + 5]
            i += 5
            
            dias, irons, stones = target.count('diamond'), target.count('iron'), target.count('stone')
            counted.append([dias, irons, stones])
        
        # 광물 우선순위: 다이아 > 철 > 돌
        counted.sort(key=lambda x: (-x[0], -x[1], -x[2]))
        return counted

    def calculate(picks, minerals):
        picks = picks[:]  # picks 리스트 복사하여 원본 변경 방지
        result = 0
        for target in minerals:
            if picks[0] > 0:  # 다이아 곡괭이
                picks[0] -= 1
                result += sum(target)
            elif picks[1] > 0:  # 철 곡괭이
                picks[1] -= 1
                result += target[0] * 5 + target[1] + target[2]
            elif picks[2] > 0:  # 돌 곡괭이
                picks[2] -= 1
                result += target[0] * 25 + target[1] * 5 + target[2]
            else:
                break
        return result

    # 필요 없는 광물 제거
    if sum(picks) * 5 < len(minerals):
        minerals = minerals[:sum(picks) * 5]
    
    scan_mineral = scan_minerals(minerals)
    answer = calculate(picks, scan_mineral)

    return answer
