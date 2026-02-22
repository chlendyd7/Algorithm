# 영단어 암기는 괴로워
import sys; input = sys.stdin.readline
n,m = map(int,input().split())
ls = []

dic = dict()
for i in range(n):
    a = input().rstrip()
    if len(a) >= m:
        if a in dic:
            dic[a] +=1
        else:
            dic[a] = 1

dic = sorted(dic.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

for i in dic:
    print(i[0])