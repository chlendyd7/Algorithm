n = int(input())
ls = []
for idx in range(n):
    age, name = input().split()
    ls.append((idx, age, name))

ls.sort(key=lambda x:(x[1], x[0]))

for idx, age, name in ls:
    print(age,name)
