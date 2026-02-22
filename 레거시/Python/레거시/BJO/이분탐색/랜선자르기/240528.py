import sys
input = sys.stdin.readline

K, N = map(int,input().split())
list = [int(input()) for _ in range(K)]

lt, rt = 0, max(list)

while lt<=rt:
    mid = (lt + rt ) // 2
    lines = 0
    for ls in list:
        lines += ls // mid
        
    if lines >= N:
        lt = mid +1
    else:
        rt = mid -1

print(rt)