'''

'''
import sys
def DFS(depth, count):
    if count>total//2:
        return
    if depth==n:
        if count==total//2:
            print("YES")
            sys.exit(0)
    else:
        DFS(depth+1, count+ls[depth])
        DFS(depth+1, count)

if __name__=='__main__':
    n=int(input())
    ls=list(map(int,input().split()))
    total=sum(ls)
    DFS(0, 0)
    print('NO')