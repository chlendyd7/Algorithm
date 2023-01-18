# DFS 문제 같으면 상태트리를 그리려고 하여야 한다
def DFS(L):
    global res
    if L==n:
        cha=max(money)-min(money)
        if cha<res:
            tmp=set() # 단 세 사람의 총액은 서로 달라야 합니다
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res=cha
    

    else:
        for i in range(3):
            money[i]+=coin[L]
            DFS(L+1)
            money[i]-=coin[L]



if __name__=="__main__":
    n=int(input())
    coin=[]
    tmp=[]
    money=[0]*3 # 3명
    res=2147000000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)
