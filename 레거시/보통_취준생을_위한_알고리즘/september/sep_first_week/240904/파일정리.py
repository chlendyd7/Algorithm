n = int(input())
dic = dict()
for _ in range(n):
    seq1, seq2 = input().split('.')
    if seq2 in dic:
        dic[seq2] += 1
    else:
        dic[seq2] = 1

sort = sorted(dic.keys())
for s in sort:
    print(s, dic[s])
