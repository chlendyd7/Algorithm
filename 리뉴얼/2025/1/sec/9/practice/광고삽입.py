def solution(play_time, adv_time, logs):
    def time_to_seconds(t):
        h, m, s = map(int, t.split(':'))
        return h * 3600 + m * 60 + s
    
    def seconds_to_time(s):
        h = s // 3600
        s %= 3600
        m = s // 60
        s %= 60
        return f"{h:02}:{m:02}:{s:02}"

    play_seconds = time_to_seconds(play_time)
    adv_seconds = time_to_seconds(adv_time)
    total_view = [0] * (play_seconds + 1)
    
    for log in logs:
        start, end = log.split('-')
        start_sec, end_sec = time_to_seconds(start), time_to_seconds(end)
        total_view[start_sec] += 1
        total_view[end_sec] -= 1
    
    for i in range(1, play_seconds + 1):
        total_view[i] += total_view[i - 1]
    
    for i in range(1, play_seconds + 1):
        total_view[i] += total_view[i - 1]
    
    max_view = total_view[adv_seconds - 1]
    start_time = 0
    for start in range(1, play_seconds - adv_seconds + 1):
        end = start + adv_seconds - 1
        current_view = total_view[end] - total_view[start - 1]
        if current_view > max_view:
            max_view = current_view
            start_time = start

    return  seconds_to_time(start_time)
