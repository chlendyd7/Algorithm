import sys


input = sys.stdin.readline

S = input().strip()
d = set()
for i in range(len(S)+1):
    for j in range(i, len(S)+1):
        d.add(S[i:j])
print(len(d)-1)
