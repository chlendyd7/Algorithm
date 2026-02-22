# 또 두 집합 A와 B에 공통으로 속하는 원소가 없을 때, 즉 A∩B＝Ø일 때 집합 A와 B는 서로소라고 한다. 예를 들어 A=｛1, 2, 3｝이고 B=｛4, 5｝일 때 A와 B는 서로소이다.
import sys
def DFS(v,s):
    if s>total//2:
        return
    if v==n:
        if s==total-s:
            print("YES")
            sys.exit(0)
        
    else:
        DFS(v+1, s+ls[v])
        DFS(v+1, s)
        





if __name__=="__main__":
    n=int(input())
    ls=list(map(int,input().split()))
    total=sum(ls)
    DFS(0, 0)
    print("NO")