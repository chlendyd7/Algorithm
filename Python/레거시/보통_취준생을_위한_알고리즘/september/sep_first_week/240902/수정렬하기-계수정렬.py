ls = [0] * 10001
n = int(input())
for i in range(n):
    num = int(input())
    ls[num] += 1
print()
for j in range(1, 10001):
    if ls[j]:
        for k in range(ls[j]):
            print(j)