
from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)
    count_lst = sorted(count.items(), key=lambda x: x[1])
    print(count_lst)
    
    answer = 0
    return answer