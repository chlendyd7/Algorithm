
from itertools import combinations, permutations, combinations_with_replacement, product


lst = [1,2,3,4,5]
for t in combinations(lst, r=3):
    print(t)

n,m = map(int, input().split())
for t in permutations(range(1,n+1), r=m):
    print(t)

for t in product(['A','B','C','D'], repeat=3):
    print(t)

