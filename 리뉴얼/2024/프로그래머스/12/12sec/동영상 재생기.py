def time_to_sec(timestamp):
    minutes, seconds = map(int, timestamp.split(':'))
    return minutes * 60 + seconds

def sec_to_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02}:{seconds:02}"

def solution(video_len, pos, op_start, op_end, commands):
    pos_sec = time_to_sec(pos)
    video_len_sec = time_to_sec(video_len)
    op_start_sec = time_to_sec(op_start)
    op_end_sec = time_to_sec(op_end)

    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec

    for cmd in commands:
        pos_sec += -10 if cmd == "prev" else 10
        pos_sec = max(0, min(pos_sec, video_len_sec))

        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

    return sec_to_time(pos_sec)
