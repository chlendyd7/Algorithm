'''
    result[-boom_len:] 부분에서 리스트 result의 끝에서 boom_len개의 요소를 
    슬라이싱하여 리스트로 가져옵니다.
'''
def boom_string(string, boom):
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

string = input()
boom = input()
print(boom_string(string, boom))
