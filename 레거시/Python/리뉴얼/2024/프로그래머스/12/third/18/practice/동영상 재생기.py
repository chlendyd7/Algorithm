def convert_sec(time):
    min, sec = map(int, time.split(':'))
    return (60 * min) + sec

def solution(video_len, pos, op_start, op_end, commands):
    video_len, pos, op_start, op_end = map(convert_sec, (video_len, pos, op_start, op_end))
    if op_start <= pos <= op_end:
        pos = op_end
    for command in commands:
        pos += -10 if command == 'prev' else 10
        if op_start <= pos <= op_end:
            pos = op_end
        if pos > video_len:
            pos = video_len
    
    min, sec = divmod(pos, 60)
    return f'{min:02}:{sec:02}'
