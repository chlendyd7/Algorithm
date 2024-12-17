n = int(input())
a = list(map(int,input().split()))
seq = [0]*n
for i in range(n):
    for j in range(n):
        if a[i]==0 and seq[j]==0:
            seq[j] = i+1