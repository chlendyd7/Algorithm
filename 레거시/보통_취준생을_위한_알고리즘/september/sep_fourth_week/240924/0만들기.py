def solution(idx, st):
    if idx == n:
        ans = eval(st.replace(' ', ''))
        if ans == 0:
            answer_lst.append(st)
        return
    else:
        idx += 1
        solution(idx, st + ' ' + str(idx))
        solution(idx, st + '+' + str(idx))
        solution(idx, st + '-' + str(idx))


t = int(input())
for _ in range(t):
    n = int(input())
    answer_lst = []
    solution(1, '1')
    for a in answer_lst:
        print(a)
    print()

