'''
    추 오른쪽에 넣고 왼쪽에 넣고
'''

def DFS(L, sum):
    global res
    if L==k:
        if 0<sum<=sum_chu:
            res.add(sum)
    else:
        DFS(L+1, sum+chu[L])
        DFS(L+1, sum-chu[L])
        DFS(L+1, sum)




if __name__=='__main__':
    k=int(input())
    chu=list(map(int,input().split()))
    sum_chu=sum(chu)
    res=set()
    DFS(0,0)
    print(sum_chu-len(res))