M,N = map(int,input().split())
ls =[]
count =[]
for i in range(M):
    ls.append(input())

for a in range(M-7): #바둑판의 시작지점을 잡음
    for b in range(N-7):
        index1=0 
        index2=0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) %2 == 0:
                    if ls[i][j] != 'W':
                        index1+=1
                    if ls[i][j] != 'B':
                        index2+=1
                else:
                    if ls[i][j] != 'B':
                        index1 +=1
                    if ls[i][j] != 'W':
                        index2 +=1
        count.append(min(index1, index2))
print(min(count))!