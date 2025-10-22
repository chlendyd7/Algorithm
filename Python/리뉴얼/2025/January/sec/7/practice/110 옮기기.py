def find_110s(string):
    stk = ''
    cnt = 0
    
    for char in string:
        stk += char
        while len(stk) > 2 and stk[-3:] == '110':
            stk = stk[:-3]
            cnt += 1
    return stk, cnt

def insert_110s(s, cnt):
    length = len(s)
    
    for i in range(length -1, -1, -1):
        if s[i] == '0':
            return s[:i+1] + '110' * cnt + s[i+1:]
    
    return '110'*cnt + s

def solution(s):
    answer = []
    for string in s:
        stk, cnt = find_110s(string)
        answer.append(insert_110s(stk, cnt))
    
    return answer
