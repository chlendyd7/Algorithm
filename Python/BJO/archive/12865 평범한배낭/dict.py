import sys

n, k = map(int, sys.stdin.readline().split())

_li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

_li.sort(reverse=True)

_dic = {0: 0}

for w, v in _li:
    temp = {}

    for bv, bw in _dic.items():
        nbw = bw + w
        nbv = bv + v
        if _dic.get(nbv, k+1) > nbw:
            temp[nbv] = nbw
    _dic.update(temp)

print(max(_dic))