'''
    1. n개 정수에서 k개를 뽑음
    2. 조합의 합이 m의 배수인 개수
    부분조합을 만들어내는 것

'''
def DFS(L, s, sum):
    global cnt
    if L==k:
        if sum%m==0:
            cnt+=1
    else:
        for i in range(s, n):
            DFS(L+1, i+1, sum+a[i])




if __name__=="__main__":
    n, k=map(int,input().split())
    a=list(map(int,input().split()))
    m=int(input())
    cnt=0
    DFS(0,0,0)
print(cnt)