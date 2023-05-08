import sys
input = sys.stdin.readline

n = int(input())
def gcd_func(a,b):
    while b != 0:
        a,b = b, a%b
    return a


def gcd(a,b):
    while b!=0:
        a,b = b, a%b
    
    return a

trees = [int(input()) for _ in range(n)]
gaps = []

for i in range(1,n):
    gaps.append(trees[i]- trees[i-1])

gaps_set = list(set(gaps))

gcd = gaps_set[0]
for i in range(1, len(gaps_set)):
    gcd = gcd_func(gcd, gaps_set[i])

answer = 0
for gap in gaps:
    answer += gap//gcd-1

print(answer)
