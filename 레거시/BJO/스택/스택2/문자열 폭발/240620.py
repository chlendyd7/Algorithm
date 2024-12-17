def boom_str(str, boom):

    boom_len = len(boom)
    stack = []
    for s in str:
        stack.append(s)
        if ''.join(stack[-boom_len:]) == boom:
            del stack[-boom_len:]
    
    result = ''.join(stack)
    if result:
        return result
    else:
        return "FRULA"


string = input()
boom = input()
print(boom_str(string, boom))