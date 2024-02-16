primeSet = set()
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def makeCombination(str1, str2):
    if str1 != "":
        if is_prime(int(str1)):
            primeSet.add(int(str1))

    for i in range(len(str2)):
        makeCombination(str1 + str2[i], str2[:i]+ str2[i+1:])
        # 두 부분 문자열을 합치면, str2에서 i에 해당하는 문자를 제외한 부분 문자열을 얻게 됩니다.

def solution(numbers):
    makeCombination("", numbers)
    return len(primeSet)

print(solution("17"))    