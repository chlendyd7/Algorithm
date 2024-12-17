from collections import defaultdict


def solution(n, k, a):
    answer = 0
    start, end = 0,0
    num_dic = defaultdict(int)

    while end < n:
        if num_dic[a[end]] >= k:
            num_dic[a[start]] -= 1
            start += 1
        else:
            num_dic[a[end]] += 1
            end += 1
            answer = max(answer, end - start)
    return answer

n, k = map(int,input().split())
lst = list(map(int,input().split()))
print(solution(n,k,lst))
