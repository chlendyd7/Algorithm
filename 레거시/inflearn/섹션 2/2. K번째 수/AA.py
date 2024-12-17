T = int(input())
for i in range(1, T+1):
    N, s ,e, k = map(int, input().split())
    l = list(map(int,input().split()))
    l = l[s-1 : e]
    print(l)
    l.sort()
    print("#%d %d" %(i, l[k-1]))
