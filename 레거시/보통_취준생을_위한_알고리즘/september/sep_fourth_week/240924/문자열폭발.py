str1 = input()
boom = input()

boom_len = len(boom)
lst = []
for i in str1:
    lst.append(i)
    if ''.join(lst[-boom_len:]) == boom:
        del lst[-boom_len:]

result = ''.join(lst)

if result:
    print(result)
else:
    print('FRULA')
