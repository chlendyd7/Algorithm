# https://www.acmicpc.net/problem/20922
from collections import defaultdict
def solution(n, k, a):
    answer = 0
    start, end = 0, 0
    num_cnt = defaultdict(int)

    while end < n:
        if num_cnt[a[end]] >= k:
            num_cnt[a[start]] -= 1
            start +=1
        else:
            num_cnt[a[end]] += 1
            end += 1
            answer = max(answer, end - start)
    return answer

n, k = map(int,input().split())
a = list(map(int,input().split()))

result = solution(n, k, a)
print(result)
