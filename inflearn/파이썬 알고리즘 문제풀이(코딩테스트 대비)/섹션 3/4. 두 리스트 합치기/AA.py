a = int(input())
b = list(map(int,input().split()))
c = int(input())
d = list(map(int,input().split()))
e = []
ai = ci = 0
while a < ai and c < ci:
    if b[ai] < d[ci]:
        e.append(b[ai])
        ai += 1
    else:
        e.append(d[ci])
        ci +=1
if ai < a:
    e = e+d[ai:]
if ci < c:
    e = e+d[ci:]
for x in e:
    print(x, end='')1