ls = [list(map(int,input().split()))for _ in range(7)]
cnt = 0 
for i in range(3):
    for j in range(7):
        tmp = ls[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt +=1
        for k in range(2):
            if ls[i+k][j] != ls[i+4-k][j]:
                break
        else:
            cnt +=1

print(cnt)

