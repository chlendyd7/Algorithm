'''
    파스칼 응용
    이항 계수의 앞
    (a+b)제곱 > 1 2 1
    (a+b)3제곱 > 1 2 2 1
'''
import sys
sys.stdin=open("input.txt", "rt")
def DFS(L, sum):
    if L==n and sum==f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i]=0

if __name__ == "__main__":
    n, f=map(int, input().split())
    p=[0]*n
    b=[1]*n #여기 초기화만 잘하면 됨
    ch=[0]*(n+1)
    for i in range(1, n):
        b[i]=b[i-1]*(n-i)//i
    DFS(0, 0)




    
