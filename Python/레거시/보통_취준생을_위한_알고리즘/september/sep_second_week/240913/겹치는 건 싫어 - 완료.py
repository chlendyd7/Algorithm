from collections import defaultdict


def solution(n, k,lst):
    check_dic = defaultdict(int)
    start, end = 0,0
    answer = 0
    while end < n:
        if check_dic[lst[end]] >= k:
            check_dic[lst[start]] -= 1
            start += 1
        else:
            check_dic[lst[end]] += 1
            end += 1
            answer = max(answer, end - start)
    return answer


n,k = map(int,input().split())
lst = list(map(int,input().split()))
print(solution(n,k,lst))