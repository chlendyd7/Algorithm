def solution(string, boom):
    result_lst = []
    boom_len = len(boom)
    
    for s in string:
        result_lst.append(s)
        if ''.join(result_lst[-boom_len:]) == boom:
            del result_lst[-boom_len:]
    result = ''.join(result_lst)
    if result:
        return result
    else:
        return 'FRULA'


str1=input()
boom=input()
print(solution(str1, boom))
