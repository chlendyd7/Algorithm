def calculate(time):
    hour,minute = map(int, time.split())
    return hour * 60 + minute

def solution(plans):
    answer = []
    stack = []
    plans = [(name, calculate(start), int(playtime)) for name, start ,playtime in plans]
    plans.sort(key=lambda x: x[1])
    prev_time = 0
    for i in range(len(plans)):
        name, start, playtime = plans[i]

        while stack:
            _name, _playtime = stack.pop()
            if prev_time >= _playtime:
                prev_time -= _playtime
                answer.append(_name)
            else:
                stack.append((_name, _playtime - prev_time))
                break
        
        stack.append((name,playtime))

        if i < len(plans) - 1:
            next_start = plans[i+1][1]
            prev_time = next_start - start
    
    while stack:
        _name, _ = stack.pop()
        answer.append(_name)
    
    return answer

