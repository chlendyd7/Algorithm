def solution(name, yearning, photo):
    score_dict = {name[i]: yearning[i] for i in range(len(name))}
    answer = []
    
    for i in range(len(photo)):
        cnt = 0
        for p in photo[i]:
            cnt += score_dict.get(p, 0)  # 기본값 0을 설정
        answer.append(cnt)
    
    return answer
