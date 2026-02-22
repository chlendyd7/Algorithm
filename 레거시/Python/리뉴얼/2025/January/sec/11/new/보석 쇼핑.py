def solution(gems):
    answer = [0, len(gems)]
    size = len(set(gems))
    left, right = 0, 0
    gem_dict = {gems[0] : 1}
    
    while left < len(gems) and right < len(gems):
        if len(gem_dict) == size:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            else:
                gem_dict[gems[left]] -= 1
                if gem_dict[gems]
            
    
    
    
    answer = []
    return answer