def get_current_degree(unit, seconds):
    if unit == 'hour':
        return (seconds % 43200) / 120
    elif unit == 'minute':
        return (seconds % 3600) / 10
    else:
        return (seconds % 60) * 6

def set_time_to_sec(h, m, s):
    sec = h * 3600 + m * 60 + s
    return sec

def solution(h1, m1, s1, h2, m2, s2):
    result = 0
    init_time, end_time = set_time_to_sec(h1, m1, s1), set_time_to_sec(h2, m2, s2)

    sec_temp, minute_temp, hour_temp = 0, 0, 0
    while init_time <= end_time: 
        hour_degree = get_current_degree('hour', init_time)
        minute_degree = get_current_degree('minute', init_time)
        sec_degree = get_current_degree('second', init_time)

        if sec_degree == 0:
            sec_degree = 360
            if minute_degree < 10:
                minute_degree += 360
            if hour_degree < 10:
                hour_degree += 360

        if sec_temp - hour_temp < 0 and sec_degree - hour_degree > 0:
            result += 1

        if sec_temp - minute_temp < 0 and sec_degree - minute_degree > 0:
            result += 1

        if sec_degree in [minute_degree, hour_degree]:
            result += 1

        init_time += 1

        hour_temp = hour_degree
        minute_temp = minute_degree
        sec_temp = sec_degree

    return result