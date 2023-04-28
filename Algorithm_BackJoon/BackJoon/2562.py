ls = []
for i in range(9):
    ls.append(int(input()))

print(max(ls))
print(ls.index(max(ls))+1)