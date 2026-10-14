'''
요금표
기본 시간(분)	기본 요금(원)	단위 시간(분)	단위 요금(원)
180	5000	10	600

출차내역 없으면 23:59에 출차된 것을 ㅗ간주
기본시간이면 기본 요금
기본요금 + 단위 시간 단위 요금
나누어떨어지지 않으면 올림

fees, records
차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열로 담아서 리턴

금액을 담는 dict
시간을 담는 dict?
'''
from math import ceil
from collections import defaultdict

def solution(fees, records):
    def change_time(time):
        hour, minu = time.split(":")
        return int(hour) * 60 + int(minu)
    
    def in_process(time, number):
        time_dict[number] = time

    def out_process(time, number):
        result_time = time - time_dict[number]
        if time <= n_time:
            amount_dict[number] += n_fee
        else:
            print(ceil((time-n_time) / c_t))
            amount_dict[number] += n_fee + ceil((time - n_time) / c_t) * c_f

    n_time, n_fee, c_t, c_f = fees
    amount_dict = defaultdict(int)
    time_dict = dict()
    
    for record in records:
        time, number, cmd = record.split(" ")
        time = change_time(time)
        if cmd == 'IN':
            in_process(time, number)
        else:
            out_process(time, number)
    
    print(amount_dict)
    
    answer = []
    return answer

def change_time(time):
    hour, minu = time.split(":")
    return int(hour) * 60 + int(minu)


from math import ceil
from collections import defaultdict

def solution(fees, records):
    n_time, n_fee, c_t, c_f = fees
    
    # 1. 누적 주차 시간과 입차 기록을 위한 딕셔너리
    duration_dict = defaultdict(int)
    in_time_dict = {}
    
    # 2. records 처리
    for record in records:
        time_str, number, cmd = record.split(" ")
        h, m = time_str.split(":")
        time = int(h) * 60 + int(m)
        
        if cmd == 'IN':
            in_time_dict[number] = time
        else:
            in_time = in_time_dict.pop(number)
            duration_dict[number] += (time - in_time)
            
    # 3. 출차 기록 없는 차량 처리 (23:59 = 1439분)
    for number, time in in_time_dict.items():
        duration_dict[number] += (1439 - time)
        
    # 4. 요금 계산 및 차량 번호 순 정렬
    result = []
    for number in sorted(duration_dict.keys()):
        total_time = duration_dict[number]
        if total_time <= n_time:
            fee = n_fee
        else:
            fee = n_fee + ceil((total_time - n_time) / c_t) * c_f
        result.append(fee)
        
    return result