'''
그림의 빨간색 선은 "죠르디"가 선택한 최적의 공익광고 위치를 나타냅니다.
만약 공익광고의 재생시간이 00시간 14분 15초라면, 위의 그림처럼 01시 30분 59초 부터 01시 45분 14초 까지 공익광고를 삽입하는 것이 가장 좋습니다. 이 구간을 시청한 시청자들의 누적 재생시간이 가장 크기 때문입니다.
01시 30분 59초 부터 01시 45분 14초 까지의 누적 재생시간은 다음과 같이 계산됩니다.
01시 30분 59초 부터 01시 37분 44초 까지 : 4번, 1번 재생 기록이 두차례 있으므로 재생시간의 합은 00시간 06분 45초 X 2 = 00시간 13분 30초
01시 37분 44초 부터 01시 45분 14초 까지 : 4번, 1번, 5번 재생 기록이 세차례 있으므로 재생시간의 합은 00시간 07분 30초 X 3 = 00시간 22분 30초
따라서, 이 구간 시청자들의 누적 재생시간은 00시간 13분 30초 + 00시간 22분 30초 = 00시간 36분 00초입니다.
'''

def solution(play_time, adv_time, logs):
    def time_to_sec(t):
        h, m, s = map(int, t.split(':'))
        return h * 3600 + m * 60 + s

    play_seconds = time_to_sec(play_time)
    adv_seconds = time_to_sec(adv_time)
    total_view = [0] * (play_seconds + 1)

    for log in logs:
        start, end = log.split('-')
        start_sec, end_sec = map(time_to_sec, [start, end])
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
        
        return start_time
