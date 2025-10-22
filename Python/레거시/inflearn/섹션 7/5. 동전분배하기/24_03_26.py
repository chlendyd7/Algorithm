
def DFS(L):
    global money, subtraction
    if L == n:
        if max(money)-min(money) < subtraction:
            subtraction = max(money)-min(money)
    else:
        for i in range(3):
            money[i]+=ls[L]
            DFS(L+1)
            money[i]-=ls[L]





if __name__=="__main__":
    n=int(input())
    ls = []
    for i in range(n):
        ls.append(int(input()))
    subtraction=1000000
    money = [0]*3