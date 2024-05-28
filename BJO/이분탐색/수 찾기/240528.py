import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))

m = int(input())
ls = list(map(int,input().split()))

A.sort()

for num in ls:
    lt, rt = 0, n-1
    is_exists = False
    
    while lt <= rt:
        mid = ( lt + rt ) // 2
        if num == A[mid]:
            is_exists = True
            print(1)
            break
        elif num > A[mid]:
            lt = mid + 1
        else:
            rt = mid - 1
    if not is_exists:
        print(0)
