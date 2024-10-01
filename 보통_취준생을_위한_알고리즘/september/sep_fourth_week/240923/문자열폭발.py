
str1 = input()
boom = input()

check_lst = []
boom_len = len(boom)
for i in range(len(str1)):
    check_lst.append(str1[i])
    print(check_lst)
    if ''.join(check_lst[-boom_len:]) == boom:
        del check_lst[-boom_len:]
result = ''.join(check_lst)
print(result if result else 'FRULA')
