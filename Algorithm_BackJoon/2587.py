import numpy

ls = []
for i in range(5):
    ls.append(int(input()))

ls.sort()
print(ls[2])
print(sum(ls)//5)
ls.sort(reverse=)