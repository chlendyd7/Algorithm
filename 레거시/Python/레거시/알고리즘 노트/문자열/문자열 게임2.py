from collections import defaultdict
def solution(w: str, k):
    max_value = -1
    min_value = float('inf')
    check_dic = defaultdict(list)
    for i in range(len(w)):
        if w.count(w[i]) >= k:
            check_dic[w[i]].append(i)
    
    if not check_dic:
        print(-1)
    else:
        for alp in check_dic:
            for i in range(len(check_dic[alp])-k+1):
                length = check_dic[alp][i+k-1] - check_dic[alp][i] + 1
                max_value = max(max_value, length)
                min_value = min(min_value, length)
        print(min_value, max_value)

T = int(input())

for _ in range(T):
    w = input()
    k = int(input())
    solution(w,k)