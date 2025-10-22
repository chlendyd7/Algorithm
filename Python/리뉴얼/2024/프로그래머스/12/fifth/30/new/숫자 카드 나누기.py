import math

def solution(arrayA, arrayB):
    answer = 0
    
    maxGCD_A = 0
    for a in arrayA:
        maxGCD_A = math.gcd(maxGCD_A, a)

    maxGCD_B = 0
    for b in arrayB:
        maxGCD_B = math.gcd(maxGCD_B, b)

    resultA = list(a % maxGCD_B == 0 for a in arrayA)
    if (resultA.count(False) == len(arrayA)):
         answer = max(answer, maxGCD_B)

    resultB = list(b % maxGCD_A == 0 for b in arrayB)
    if (resultB.count(False) == len(arrayB)):
        answer = max(answer, maxGCD_A)

    return answer
