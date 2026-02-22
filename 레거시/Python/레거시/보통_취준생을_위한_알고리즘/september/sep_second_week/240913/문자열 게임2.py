from collections import defaultdict


def solution(st, k):
    min_v = float('inf')
    max_v = -1
    check_dic = defaultdict(list)
    for i in range(len(st)):
        if st.count(st[i]) >= k:
            check_dic[st[i]].append(i)
    if not check_dic:
        print(-1)
    else:
        for alp in check_dic:
            for i in range(len(check_dic[alp])-k+1):
                length = check_dic[alp][i+k-1] - check_dic[alp][i] + 1
                min_v = min(min_v, length)
                max_v = max(max_v, length)

        print(min_v, max_v)

t = int(input())
for _ in range(t):
    string = input()
    k = int(input())
    solution(string, k)