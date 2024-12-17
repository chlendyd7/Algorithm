def solution(name, yearing, photo):
    score_dict = {name[i]: yearing[i] for i in range(len(name))}
    answer = []
    
    for i in range(len(photo)):
        cnt = 0
        for p in photo[i]:
            cnt += score_dict.get(p, 0)
        answer.append(cnt)
        
    return answer
