import sys
input = sys.stdin.readline
name = input().strip()
n = int(input())

ls = [[0 for _ in range(26)] for _ in range(len(name))]
ls[0][ord(name[0])-97] = 1
for i in range(1, len(name)):
    ls[i][ord(name[i])-97] = 1
    for j in range(26):
        ls[i][j] += ls[i-1][j]

for k in range(n):
    a = input().split()
    alp = ord(a[0]) - 97
    if int(a[1]) > 0:
        result = ls[int(a[2])][alp] - ls[int(a[1])-1][alp]
    else:
        result = ls[int(a[2])][alp]
    print(result)
