first = input()
second = input()
p1 = dict()
p2 = dict()

for i in first:
    p1[i] = p1.get(i,0)+1

for i in second:
    p2[i] = p2.get(i,0)+1

for i in p1.keys():
    if i in p2.keys():
        if p1[i] != p2[i]:
            print("NO")
            break
    else:
        print("NO")
else:
    print("YES")

        