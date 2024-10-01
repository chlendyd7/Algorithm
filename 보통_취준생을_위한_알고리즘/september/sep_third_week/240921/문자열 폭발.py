str1 = list(input())
boom = input()


boom_len = len(boom)
check_lst = []
for s in str1:
    check_lst.append(s)
    if ''.join(check_lst[-boom_len:]) == boom:
        del check_lst[-boom_len:]
result = ''.join(check_lst)
if result:
    print(result)
else:
    print('FRULA')
