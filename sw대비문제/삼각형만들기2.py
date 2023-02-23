import sys
input = sys.stdin.readline

tr = []
for _ in range(int(input())):
    tr.append(int(input()))
tr.sort(reverse=True)

for i in range(len(tr)-2):
    if tr[i] < sum(tr[i+1:i+3]):
        print(sum(tr[i:i+3]))
        break
else:
    print(-1)

