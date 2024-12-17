from collections import defaultdict


N, d, k, c = map(int,input().split())
chbobs = [int(input()) for _ in range(N)]
chbobs += chbobs[:N-1]
answer = 0

for i in range(N):
    num = len(set(chbobs[i:i+k] + [c]))
    answer = max(answer, num)

print(answer)