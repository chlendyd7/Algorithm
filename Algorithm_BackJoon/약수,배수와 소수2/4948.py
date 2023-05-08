import sys
input = sys.stdin.readline

while True:
    n = int(input())
    cnt = 0
    if n == 0 :
        break
    if n == 1:
        print(1)
    else:
        for i in range(n,2*n+1):
            for j in range(2,int(i**0.5)+1):
                if i % j == 0:
                    break
                else:
                    cnt +=1
        print(cnt)            