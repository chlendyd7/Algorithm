import sys
N = list(map(int, sys.stdin.readline().strip()))
R = list(map(int, sys.stdin.readline().strip()))
print(N)
print(R)
result = []
ncnt = [0] * 10
ecnt = [0] * 10

for i in N:     
    ncnt[i] += 1

for i in R:
    ecnt[i] += 1

for i in N:
    if ecnt[i] and ecnt[i] == ncnt[i]:
        ncnt[i] -= 1
        ecnt[i] -= 1
    else :
        while result:
            if result[-1] >= i or not ecnt[result[-1]]:
                break
            ecnt[result[-1]] -= 1
            result.pop()
        ncnt[i] -= 1
        result.append(i)
print(*result, sep= "")
# 출처: https://edder773.tistory.com/285 [개발하는 차리의 학습 일기:티스토리]