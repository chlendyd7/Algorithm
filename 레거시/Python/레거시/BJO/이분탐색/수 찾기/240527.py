import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
m = int(input())
ls = list(map(int,input().split()))    

A.sort()

for num in ls:
    lt, rt = 0, n-1
    isexist = False
    
    while lt <= rt:
        mid = (lt + rt ) // 2
        if num == A[mid]:
            isexist = True
            print(1)
            break
        elif num > A[mid]:
            lt = mid + 1
        else:
            rt = mid - 1
    if not isexist:
        print(0)
