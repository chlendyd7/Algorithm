#☆☆☆

def DFS(L, sum):
    global cnt
    if L==k: # 동전의 갯수
        if sum==T:
            cnt+=1
        else:
            for i in range(cn[L]+1):
                DFS(L+1, sum+(cv[L]*i)) # 1을 곱하기 위해





if __name__=="__main__":
    T=int(input())
    k=int(input())
    cv = list()
    cn = list()
    for i in range(k):
        a, b = map(int, input().split())
        cv.append(a)
        cv.append(b)
    cnt = 0
    DFS(0,0)