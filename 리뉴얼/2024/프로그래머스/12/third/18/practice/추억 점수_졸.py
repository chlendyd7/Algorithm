def solution(name, yearning, photo):
    n = len(name)
    dic = { name[i] : yearning[i] for i in range(n)}
    answer = []
    
    for pp in photo:
        cnt = 0
        for p in pp:
            cnt += dic.get(p, 0)
        answer.append(cnt)
    return answer