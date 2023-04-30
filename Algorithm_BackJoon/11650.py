n = int(input())

ls = [list(map(int,input().split()))for _ in range(n)]
ls.sort()
for x,y in ls:
    print(x,y)