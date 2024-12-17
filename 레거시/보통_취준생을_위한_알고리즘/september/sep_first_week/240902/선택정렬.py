n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    for j in range(1+1, n):
        if arr[i]>arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

for i in arr:
    print(i)
