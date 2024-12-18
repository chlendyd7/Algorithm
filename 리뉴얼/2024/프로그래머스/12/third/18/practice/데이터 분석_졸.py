def solution(data, ext, val_ext, sort_by):
    ext_dict = { 'code' : 0, 'date' : 1, 'maximum' : 2, 'remain' : 3 }
    data_list = []

    for d in data:
        if d[ext_dict[ext]] < val_ext:
            data_list.append(d)
    
    data_list.sort(key=lambda x:x[ext_dict[sort_by]])

    return data_list
