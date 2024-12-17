def solution(S, T):
    int_S = int(S.replace(':', ''))
    int_T = int(T.replace(':', ''))
    cnt = 0
    for num in range(int_S, int_T+1):
        lst_num = list(str(num))
        set_num = set(lst_num)
        if len(set_num) <= 2:
            cnt += 1
    return cnt
S ='22:22:21'
T = '22:22:23'
print(solution(S,T))