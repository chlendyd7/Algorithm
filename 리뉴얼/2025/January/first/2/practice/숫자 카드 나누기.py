import math
from functools import reduce
def solution(arrayA, arrayB):
    gcd_a = reduce(math.gcd, arrayA)
    gcd_b = reduce(math.gcd, arrayB)
    answer = 0
    result_a = [a % gcd_b == 0 for a in arrayA]
    if result_a.count(False) == len(arrayA):
        answer = max(answer, gcd_b)
    
    result_b = [b % gcd_a == 0 for b in arrayB]
    if result_b.count(False) == len(arrayB):
        answer = max(answer, gcd_a)
    return answer
