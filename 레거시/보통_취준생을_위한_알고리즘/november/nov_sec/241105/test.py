from functools import cmp_to_key

# 비교 함수 정의
def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0

# 문자열 배열
arr = ["3", "30", "34", "5", "9"]

# cmp_to_key를 사용하여 비교 함수를 키 함수로 변환
arr.sort(key=cmp_to_key(compare))

print(arr)

n = int(input())
arr = list(input() for _ in range(n))
print(arr.pop(0))
