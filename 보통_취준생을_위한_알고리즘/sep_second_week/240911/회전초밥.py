



from collections import defaultdict


def solution(n,k,c, chobob):
    check_dic = defaultdict(int)
    check_dic[c] = 1
    start, end = 0, k
    while end < n:
        check_dic[chobob[end]] += 1
        end += 1
    max_sushi = len(check_dic)
    
    for _ in range(n):
        max_sushi = max(max_sushi, len(check_dic))
        
        check_dic[chobob[end]] += 1
        check_dic[chobob[start]] -= 1
        if check_dic[chobob[start]] == 0:
            del check_dic[chobob[start]]
        
        start += 1
        end += 1
    return max_sushi
n, d, k, c = map(int,input().split())
chobob = [int(input()) for _ in range(n)]
chobob += chobob[:n-1]
print(solution(n,k,c,chobob))