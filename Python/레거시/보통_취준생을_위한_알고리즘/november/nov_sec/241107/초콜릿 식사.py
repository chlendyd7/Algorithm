'''
    초콜릿은 2 제곱
    상근: k개의 정사각형을 먹어야 함
    선영: 상근이가 주는 초콜릿만 먹음
    K개 정사각형이 되도록 쪼갬
    D/2로 쪼개진다?
'''
k = int(input())
x = [2**i for i in range(21)]
for i in x:
    if k <= i:
        choco = i
        break
cnt = 0
temp = choco
if k != choco:
    while k:
        temp //= 2
        if k >= temp:
            k -= temp
            cnt += 1
        else:
            cnt += 1
print(choco, cnt)
