def solution(name, yearning, photo):
    name_dict = dict()
    answer = []
    for i in range(len(name)):
        name_dict[name[i]] = yearning[i]
    
    for pp in photo:
        cnt = 0
        for p in pp:
            cnt += name_dict.get(p, 0)
        answer.append(cnt)
    return answer