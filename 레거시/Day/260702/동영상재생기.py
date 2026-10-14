'''
    시간이 간건
    sec, min 따로 관리는 안됨 시작시간, 나가는 시간 조건 때문에
    그냥 min을 sec로 바꿔서 관리하고 마지막에 바꾸기
'''

def solution(video_len, pos, op_start, op_end, commands):
    video_len = convert_second(video_len)
    op_start = convert_second(op_start)
    op_end = convert_second(op_end)
    pos = check(convert_second(pos), video_len, op_start, op_end)
    
    for c in commands:
        if c == 'next':
            pos += 10
        else:
            pos -= 10
        pos = check(pos, video_len, op_start, op_end)
            
    
    return return_second(pos)


def convert_second(time):
    split_time = time.split(":")
    minu = int(split_time[0])
    sec = int(split_time[1])
    
    
    return minu * 60 + sec

def return_second(time):
    minu = str(time // 60)
    sec = str(time % 60)
    
    if len(minu) < 2:
        minu = "0" + minu
    
    if len(sec) < 2:
        sec = "0" + sec
    
    return minu + ":" + sec


def check(time, video_len, op_start, op_end):
    if 0 > time:
        time = 0
    if time > video_len:
        time = video_len
    if op_start <= time <= op_end:
        time = op_end
    return time



def solution(video_len, pos, op_start, op_end, commands):
    # 헬퍼 함수 정의 (안쪽으로 넣어 가독성 향상)
    def to_sec(time):
        m, s = map(int, time.split(":"))
        return m * 60 + s

    def apply_rules(t, v_len, op_s, op_e):
        # 1. 오프닝 구간 체크 (가장 먼저 수행되어야 함)
        if op_s <= t <= op_e:
            t = op_e
        # 2. 범위를 벗어나는지 체크
        return max(0, min(t, v_len))

    # 초 변환
    v_len = to_sec(video_len)
    op_s = to_sec(op_start)
    op_e = to_sec(op_end)
    pos = apply_rules(to_sec(pos), v_len, op_s, op_e)

    for c in commands:
        pos += 10 if c == 'next' else -10
        pos = apply_rules(pos, v_len, op_s, op_e)

    # 문자열로 변환 (f-string 사용)
    return f"{pos // 60:02d}:{pos % 60:02d}"