'''
    무거우면 버리기?
'''
def DFS(depth, max, tsum):
    global result
    if result>max+(total-tsum):
        return
    if max>c:
        return
    if max < c and result<max:
        result=max
    if depth==n:
        if max>result:
            result=max
    else:
        DFS(depth+1, max+ls[depth], tsum+ls[depth])
        DFS(depth+1, max, tsum+ls[depth])


if __name__=='__main__':
    c, n=map(int, input().split())
    result=0
    ls=[]
    for _ in range(n):
        ls.append(int(input()))
    total=sum(ls)
    DFS(0,0,0)
    print(result)
    