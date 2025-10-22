def solution(idx, string:str):
    if idx == n:
        result = eval(string.replace(' ', ''))
        if result == 0:
            result_lst.append(string)
    else:
        idx += 1
        solution(idx, string + ' ' + str(idx))
        solution(idx, string + '+' + str(idx))
        solution(idx, string + '-' + str(idx))




t = int(input())
for _ in range(t):
    n = int(input())
    result_lst = []
    solution(1, '1')
    for r in result_lst:
        print(r)
    print()
