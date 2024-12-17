N = list(map(int, input()))
R = list(map(int, input()))
result = []
ncnt = [0] * 10
ecnt = [0] * 10

for i in N:
    ncnt[i] += 1
for i in R:
    ecnt[i] += 1

result = []
for i in N:
    if ecnt[i] and ecnt[i] == ncnt[i]:
        ecnt[i] -= 1
        ncnt[i] -= 1
    else:
        while result:
            if result[-1] >= i or not ecnt[result[-1]]:
                break
            ecnt[result[-1]] -= 1
            result.pop()
        ncnt[i] -= 1
        result.append(i)
print(*result, sep='')
