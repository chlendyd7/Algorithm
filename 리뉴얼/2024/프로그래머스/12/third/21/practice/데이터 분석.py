def solution(data, ext, val_ext, sort_by):
    
    idx_dict = dict(
        code = 0,
        date = 1,
        maximum = 2,
        remain = 3
    )
    
    answer = []
    for d in data:
        if d[idx_dict[ext]] < val_ext:
            answer.append(d)
    answer.sort(key=lambda x:x[idx_dict[sort_by]])
    return answer