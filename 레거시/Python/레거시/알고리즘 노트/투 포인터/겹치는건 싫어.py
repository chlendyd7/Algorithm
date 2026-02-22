from collections import defaultdict

def solution(n, k, ls):
    answer = 0
    check_dict = defaultdict(int)
    start, end = 0, 0
    while end < n:
        if check_dict[ls[end]] < k:
            check_dict[ls[end]] += 1
            end += 1
        else:
            check_dict[ls[start]] -=1
            start += 1
        answer = max(answer, end-start)

    return answer    

n,k = map(int,input().split())
ls = list(map(int,input().split()))
print(solution(n,k,ls))
