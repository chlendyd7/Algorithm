def convert_time(time):
    minute, seconds = map(int, time.split(":"))
    return seconds + (minute * 60)

def solution(video_len, pos, op_start, op_end, commands):
    video_len = convert_time(video_len)
    pos = convert_time(pos)
    op_start = convert_time(op_start)
    op_end = convert_time(op_end)
    
    if op_start <= pos <= op_end:
        pos = op_end
    
    for command in commands:
        pos += -10 if command == 'prev' else 10
        pos = max(0, min(pos, video_len))
        
        if op_start <= pos <= op_end:
            pos = op_end

    minute, second = divmod(pos, 60)
    return f"{minute:02}:{second:02}"
