arr = [1,2,3,4]
print(f'부분 집합의 수: {1 << len(arr)}')

for i in range(1 << len(arr)):
    for idx in range(len(arr)):
        # i: 부분 집합 번호 (각 자리의 포함 여부)
        # (1 << idx): 0b1, 0b10, 0b100
        if i & (1 << idx):
            print(arr[idx], end=' ')
    print()


# 0, 0000
# 1, 0001
# 2, 0010
# 3, 0011