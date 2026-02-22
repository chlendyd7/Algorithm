'''
    1. stack을 이용
    2. 시간을 바꿈
    3. 그 전 시간을 빼기
    4. 모든 시간이 빼졌으면 result에 담기
'''
def calculate(time):
    hour,minute = map(int, time.split(':'))
    return hour * 60 + minute

def solution(plans):
    stack = []
    answer = []
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        st = h*60+m
        plans[i][1] = st
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x : x[1])
    
    for i in range(len(plans)):
        if i == len(plans) - 1:
            stack.append(plans[i])
            break
        sub, st, t = plans[i]
        nsub, nst, nt = plans[i+1]

        if st + t <= nst:
            answer.append(sub)
            temp_time = nst - (st + t)

            while temp_time != 0 and stack:
                tsub, tst, tt = stack.pop()
                if temp_time >= tt:
                    answer.append(tsub)
                    temp_time -= tt
                else:
                    stack.append([tsub, tst, tt - temp_time])
                    temp_time = 0
        else:
            plans[i][2] = t - (nst - st)
            stack.append(plans[i])
    while stack:
        sub, st, tt = stack.pop()
        answer.append(sub)

    return answer

print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))