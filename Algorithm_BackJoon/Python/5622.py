a = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
b = input()
cnt = 0

for i in range(len(b)):
    for j in a:
        if b[i] in j:
            cnt += a.index(j)+3
print(cnt)