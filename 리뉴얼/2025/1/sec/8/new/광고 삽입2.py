def solution(play_time, adv_time, logs):
    def time_to_seconds(t):
        h, m, s = map(int, t.split(':'))
        return h * 3600 + m * 60 + s
    
    play_seconds = time_to_seconds(play_time)
    adv_time = time_to_seconds(adv_time)
    total_view = [0] * (play_seconds + 1)

    for log in logs:
        start, end = log.split('-')
        start_sec = time_to_seconds(start)
        end_sec = time_to_seconds(end)
        total_view[start_sec] += 1
        total_view[end_sec] -= 1
    
    for