a = input()
b = input()
b1 = dict()
b2 = dict()

for i in a:
    b1[i] = b1.get(i,0)+1

for i in b:
    b2[i] = b2.get(i,0)+1

for i in b1.keys():
    if i in b2.keys():
        if b1[i] != b2[i]:
            print("NO")
            break
    else:
        print("NO")
else:
    print("YES")

a = input()
b = input()
sH = dict()
for x in a:
    sH[x] = sH.get(x,0)+1

for x in b:
    sH[x] = sH.get(x,0)-1

for x in a:
    if sH.get(x)>0:
        print("NO")
        break
    else:
        print("YES")

