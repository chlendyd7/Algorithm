a = input()
b = list(map(int,input().split()))
c = input()
d = list(map(int,input().split()))
e = []

for i in b:
    e.append(i)
for j in d:
    e.append(j)

e.sort()
for z in e:
    print(z, end =" ")