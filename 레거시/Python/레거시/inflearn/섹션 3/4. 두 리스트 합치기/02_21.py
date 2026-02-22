n1 = int(input())
l1 = list(map(int,input().split()))
n2 = int(input())
l2 = list(map(int,input().split()))
e = []
ai = ci = 0
while n1 < ai and n2 < ci:
    if l1[ai] < l2[ci]:
        e.append(l1[ai])
        ai +=1
    else:
        e.append(l2[ci])
        ci +=1

if ai < n1:
    e = e+l1[n1:]
if ci < n2:
    e = e+l2[n2:]
for x in c:
    print(x, end=' ')