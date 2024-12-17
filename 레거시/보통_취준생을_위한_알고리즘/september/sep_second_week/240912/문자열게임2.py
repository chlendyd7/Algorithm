from collections import defaultdict


def solution(string: str, k):
    snall = 10000
    big = 1
    check_dic = defaultdict(list)
    answer_list = []
    for i in range(len(string)):
        if string.count(string[i]) >= k:
            check_dic[string[i]].append(i)
    if not check_dic:
        print(-1)
    for dic in check_dic:
        print('checkdic:', check_dic)
        print(dic)
        answer_list.append(dic[-1] - dic[0] + 1)
    print(*answer_list)

t = int(input())
for _ in range(t):
    string = input()
    k = int(input())
    solution(string, k)
