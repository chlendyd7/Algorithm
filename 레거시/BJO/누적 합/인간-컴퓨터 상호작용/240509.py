import sys
input = sys.stdin.readline
string = input().strip()
ls = [[0 for _ in range(26)] for _ in range(len(string))]

ls[0][ord(string[0])-97] = 1
for i in range(1, len(string)):
    ls[i][ord(string[i])-97] = 1
    for j in range(26):
        ls[i][j] += ls[i-1][j]

q = int(input())
for k in range(q):
    a = input().split()
    if int(a[1]) > 0 :
        res = ls[int(a[2])][ord(a[0])-97] - ls[int(a[1])-1][ord(a[0])-97]
    else:
        res = ls[int(a[2])][ord(a[0])-97]
    print(res)
