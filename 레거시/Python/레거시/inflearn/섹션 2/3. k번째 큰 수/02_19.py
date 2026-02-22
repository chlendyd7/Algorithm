import itertools


n, k = map(int,input().split())
l = list(map(int,input().split()))
l.sort(reverse=True)
combinations = set(map(sum, itertools.combinations(l, 3)))
combinations = list(combinations)
combinations.sort(reverse=True)
print(combinations[k-1])