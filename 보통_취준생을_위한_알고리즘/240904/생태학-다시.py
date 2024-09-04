# https://www.acmicpc.net/problem/4358

import sys

tree = {}
total = 0
while True:
    word = sys.stdin.readline().rstrip()
    if word == '':
        break
    total += 1
    if word in tree:
        tree[word] += 1
    else:
        tree[word] = 1

sorted_trees = sorted(tree.keys())
for word in sorted_trees:
    percent = tree[word]/total * 100
    print(f'{word} {percent:.4f}' )
