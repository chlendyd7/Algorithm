from collections import Counter


def solution(a):
    elements = Counter(a)
    
    answer = 0
    for k in elements.keys():
        if elements[k] <= answer:
            continue
        cnt = 0
        idx = 0
        while idx < len(a) - 1:
            
            if (a[idx] == k or a[idx+1] == k) and a[idx] != a[idx+1]:
                cnt += 1
                idx += 2
            else:
                idx += 1
        
        answer = max(cnt, answer)
    
    return answer * 2
