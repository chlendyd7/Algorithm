a, b = input().split()
result = float('inf')
for i in range(len(b)-len(a)+1):
    temp = 0
    for j in range(len(a)):
        if b[i+j] != a[j]:
            temp += 1
    result = min(result, temp)
print(result)
