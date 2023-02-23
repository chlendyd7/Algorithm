n = int(input())
u = set()
ans=[]
for i in range(n):
    u.add(int(input()))
sums = set()
for i in u:
    for j in u:
        sums.add(i + j)
for i in u:
    for j in u:
        if (i - j) in sums:
            ans.append(i)
ans.sort()
print(ans[-1])