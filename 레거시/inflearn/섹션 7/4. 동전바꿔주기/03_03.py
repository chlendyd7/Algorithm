def DFS(L, sum):
    global cnt
    if L==k:
        if sum==T:
            cnt+=1
    else:
        for i in range(cn[L]+1):
            DFS(L+1, sum+cv[L]*i)




if __name__=="__main__":
    T = int(input())# 총합 금액
    k = int(input())# 동전 갯수
    cv = list()
    cn = list()
    for i in range(k):
        a, b = map(int,input().split())
        cv.append(a)
        cn.append(b)
    cnt = 0
    DFS(0,0)
    print(cnt)
    