def DFS(level):
    if check[level]>0:
        return check[level]
    if level==1 or level==2:
        return level
    else:
        check[level]=DFS(level-1)+DFS(level-2)
        return check[level]
    



if __name__=='__main__':
    n=int(input())
    check=[0]*(n+1)
    print(DFS(n))
    print(check[n])