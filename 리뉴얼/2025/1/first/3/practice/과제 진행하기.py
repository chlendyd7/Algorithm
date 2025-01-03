def solution(plans):
    calculate_plan = []
    answer = []
    for p in plans:
        s, t, rt = p[0], p[1], p[2]
        m, s = map(int, t.split(':'))
        t = m+s
        calculate_plan.append([s, t, int(rt)])
    stack = []
    for i in range(len(calculate_plan)):
        if i == len(calculate_plan) -1 :
            stack.append([calculate_plan[i][0], calculate_plan[i][2]])
            break
        s, t, rt = calculate_plan[i]
        ns, nt, nrt = calculate_plan[i+1]
        
        
        remain_time = 0
        if t + rt < nt:
            remain_time = nt - (t + rt)
            answer.append(s)
        else:
            stack.append([s, (t+rt)-nt])
            continue

        while stack:
            ts, trt = stack.pop()
            if trt <= remain_time:
                answer.append(ts)
                remain_time -= trt
            else:
                trt -= remain_time
                stack.append([ts, trt])                
                break
    if stack:
        answer.append(stack.pop()[0])
    return answer
solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]])