
from collections import defaultdict


def solution(n,k,ls):
    answer = 0
    start = 0
    end = 0
    check_dic = defaultdict(int)
    
    while end < n:
        if check_dic[ls[end]] >= k:
            check_dic[ls[start]] -= 1
            start += 1
        else:
            check_dic[ls[end]] += 1
            end += 1
            answer = max(answer, end-start)
    return answer


n,k = map(int,input().split())
ls = list(map(int,input().split()))
print(solution(n,k,ls))