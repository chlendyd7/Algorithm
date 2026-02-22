def boom_string(string, boom):
    boom_len = len(boom)
    
    result = []
    for s in string:
        result.append(s)
        if ''.join(result[-boom_len:]) == boom:
            del result[-boom_len:]
    result = ''.join(result)
    if result:
        return result
    else:
        return 'FRULA'

string = input()
boom = input()
print(boom_string(string, boom))

