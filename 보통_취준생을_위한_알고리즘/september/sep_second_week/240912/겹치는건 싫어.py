from collections import defaultdict


n, k = map(int,input().split())
lst = list(map(int,input().split()))
check_dic = defaultdict(int)
left, right = 0, 0
answer = 0
while right < n:
    if check_dic[lst[right]] < k:
        check_dic[lst[right]] += 1
        right += 1
        answer = max(answer, right - left)
    else:
        check_dic[lst[left]] -= 1
        left += 1
print(answer)