def find_110s(string):
    temp = ''
    cnt = 0

    for char in string:
        temp += char
        while len(temp) > 2 and temp[-3:] == '110':
            temp = temp[:-3]
            cnt += 1
    return temp, cnt

def insert_110s(string, cnt):
    length = len(string)

    for i in range(length -1, -1, -1):
        if string[i] == '0':
            return string[:i+1] + '110' * cnt + string[i+1:]
    return '110' * cnt + string

def solution(s):
    answer = []
    for string in s:
        string, cnt = find_110s(string)
        answer.append(insert_110s(string, cnt))
    
    return answer
