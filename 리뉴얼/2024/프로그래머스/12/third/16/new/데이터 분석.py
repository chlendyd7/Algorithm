def solution(data, ext, val_ext, sort_by):

    ext = {'code': 0, 'date': 1, 'maximum': 2}.get(ext, 3)
    print(ext)

    answer = []
    for da in data:
        if da[ext] < val_ext:
            answer.append(da)

    sort = {'code': 0, 'date': 1, 'maximum': 2}.get(sort_by, 3)
    answer.sort(key=lambda x: x[sort])
    return answer
