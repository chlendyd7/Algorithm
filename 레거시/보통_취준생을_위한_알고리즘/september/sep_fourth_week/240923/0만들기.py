def solution(idx, rst):
    if idx == n:
        answer = eval(rst.replace(' ', ''))
        if answer == 0:
            ans_lst.append(rst)
        return
    else:
        idx += 1
        solution(idx, rst + ' '+ str(idx))
        solution(idx, rst + '+'+ str(idx))
        solution(idx, rst + '-'+ str(idx))



T = int(input())
ans_lst = []
for _ in range(T):
    n = int(input())
    solution(1, '1')
    for a in ans_lst:
        print(a)
    print()
