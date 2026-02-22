import sys
input = sys.stdin.readline

N,M = map(int,input().split())
trees = list(map(int,input().split()))

lt, rt = 0, max(trees)

while lt <= rt:
    mid = (lt + rt) // 2
    count = 0
    for tree in trees:
        if tree >= mid:
            count += tree - mid
    
    if count >= M:
        lt = mid + 1
    else:
        rt = mid - 1

print(rt)