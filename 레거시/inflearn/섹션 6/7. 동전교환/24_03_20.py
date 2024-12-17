'''
    더하면서 현재보다 작으면 버리기
'''



def DFS(depth, amount):
    global cnt
    if amount > m:
        return
    if depth>cnt:
        return
    if amount == m:
        if depth<cnt:
            cnt=depth
    else:
        for i in range(n):
            DFS(depth+1, amount+ls[i])

n=int(input())
ls=list(map(int,input().split()))
m=int(input())
cnt=1000000
ls.sort(reverse=True)
DFS(0,0)
print(cnt)