n = int(input())
s = set()
ls =[]
for i in range(n):
    s.add(int(input()))

sm = set()
for i in s:
    for j in s:
        if i !=j:
            sm.add(i+j)

for i in s:
    for j in s:
        if i !=j:
            if i-j in sm:
                ls.append(i)
ls.sort()
if ls:
    print(ls[-1])
else:
    print(0)
