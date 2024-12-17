T = int(input())
for i in range(1, T+1):
    N, s ,e, k = map(int, input().split())
    l = list(map(int,input().split()))
    l.sort()
    print( "#%d %d" %(i, l[k]))
