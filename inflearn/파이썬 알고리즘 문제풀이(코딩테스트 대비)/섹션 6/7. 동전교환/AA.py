<<<<<<< HEAD
def DFS(L, sum):
    global res
    if sum > m:
        return
    if L > res:
        return
    if sum == m:
        if L<res:
            res = L
=======
def DFS(L,sum):
    global cnt
    if L >= cnt:
        return
    if sum>res:
        return
    if sum==res:
        if L<cnt:
            cnt=L
>>>>>>> 8180045cc69c5d51e320377eb4095b6bfa70c5a7
    else:
        for i in range(n):
            DFS(L+1, sum+ls[i])








if __name__=="__main__":
    n = int(input())
<<<<<<< HEAD
    a = list(map(int, input().split()))
    m = int(input())
    res = 100000
    a.sort(reverse=True)
=======
    ls = list(map(int,input().split()))
    res = int(input())
    cnt = 10000000
    ls.sort(reverse=True)
>>>>>>> 8180045cc69c5d51e320377eb4095b6bfa70c5a7
    DFS(0,0)
    print(cnt)
