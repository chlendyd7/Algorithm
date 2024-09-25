
def solution(idx, lst):
    if idx == N:
        if eval(lst.replace(' ', '')) == 0:
            answer_lst.append(lst)
        return
    else:
        solution(idx+1, lst + ' ' + str(idx+1))
        solution(idx+1, lst + '+' + str(idx+1))
        solution(idx+1, lst + '-' + str(idx+1))

T = int(input())
for _ in range(T):
    N = int(input())
    answer_lst = []
    solution(1, '1')
    for a in answer_lst:
        print(a)
    print()
