import sys

input = sys.stdin.readline

n = int(input())

ls = []

for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    ls.append((age,name))

ls.sort(key = lambda x:x[0])
for x,y in ls:
    print(x,y)