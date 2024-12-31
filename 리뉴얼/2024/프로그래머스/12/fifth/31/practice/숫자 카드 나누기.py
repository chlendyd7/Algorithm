import math


def solution(arrayA, arrayB):
    answer = 0

    maxGCD_A = 0
    for a in arrayA:
        maxGCD_A = math.gcd(maxGCD_A, a)

    maxGCD_B = 0
    for b in arrayB:
        maxGCD_B = math.gcd(maxGCD_B, b)
    
    result_a = list(a % maxGCD_B == 0 for a in arrayA)
    if result_a.count(False) == len(arrayA):
        answer = max(answer, maxGCD_B)
    
    result_b = list(b % maxGCD_A == 0 for b in arrayB)
    if result_b.count(False) == len(arrayB):
        answer = max(answer, maxGCD_A)
    

    return answer
