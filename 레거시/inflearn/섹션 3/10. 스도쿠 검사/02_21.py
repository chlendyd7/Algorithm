def check(x):
    for i in range(9):
        dy1 = [0]*10
        dy2 = [0]*10
        for j in range(9):
            dy1[x[i][j]]=1
            dy2[x[j][i]]=1
        
        if sum(dy1) != 9 or sum(dy2) != 9:
            return False
        
    for i in range(3):
        for j in range(3):
            dy3 = [0]*10
            for z in range(3):
                for y in range(3):
                    dy3[x[i*3+z][j*3+y]]=1
            if sum(dy3) != 9:
                return False
    return True
                    
            

        







board = [list(map(int,input().split())) for _ in range(9)]


if check(board):
    print("YES")
else:
    print("NO")
