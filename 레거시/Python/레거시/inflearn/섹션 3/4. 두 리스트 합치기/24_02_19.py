n1 = int(input())
a = list(map(int, input().split()))
n2 = int(input())
b = list(map(int, input().split()))
c = []
p1 = p2 = 0
while p1<n1 and p2<n2:
    if a[p1] < b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1<n1:
    c = c+a[p1:]
elif p2<n2:
    c = c+b[p2:]
for _ in c:
    print(_, end=' ')
# c = a+b
# c.sort()
# for _ in c:
#     print(_, end=' ')

