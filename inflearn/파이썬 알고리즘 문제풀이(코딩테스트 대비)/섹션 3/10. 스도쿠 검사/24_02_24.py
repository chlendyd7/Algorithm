ls = [list(map(int,input().split()))for _ in range(9)]
result = True
for i in range(9):
    check1 = [0]*10
    check2 = [0]*10
    for j in range(9):
        check1[ls[i][j]] = 1
        check2[ls[j][i]] = 1
    if sum(check1) != 9 or sum(check2) != 9:
        result = False
for i in range(3):
    for j in range(3):
        check3 = [0]*10
        for k in range(3):
            for s in range(3):
                check3[ls[i*3+k][j*3+s]] = 1
        if sum(check3) != 9:
            result = False
if result:
    print("YES")
else:
    print("NO")
