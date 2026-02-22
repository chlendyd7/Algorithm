def DFS(L):
    global res
    if L == N:
        cha = max(money) - min(money)
        if cha < res:
            tmp=set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha
    
    else:
        for i in range(3):
            money[i]+=coin[L]
            DFS(L+1)
            money[i]-=coin[L]





if __name__=="__main__":
    N = int(input())
    coin = []
    money = [0]*3
    for i in range(N):
        coin.append(int(input()))
    res = 21470000
    DFS(0)
    print(res)