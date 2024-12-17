import sys
from collections import defaultdict

cnt = 0
trees = defaultdict(int)
while True:
    word = sys.stdin.readline().rstrip()
    if word == '':
        break
    cnt += 1
    trees[word] += 1

sortred_trees = sorted(trees.keys())
for tree in sortred_trees:
    tree_percent = trees[tree] / cnt * 100
    print(f'{tree} {tree_percent:.4f}')
