a = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
b = input()
for j in a:
    b = b.replace(j, '*')
print(len(b))
        