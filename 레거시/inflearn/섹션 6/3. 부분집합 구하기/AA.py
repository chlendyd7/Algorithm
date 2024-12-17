import sys
#sys.stdin=open("input.txt", "r")
def DFS(v):
    if v==n+1:
        for i in range(0, n+1):
            if ch[i]==1:
                print(i, end=' ')
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)

if __name__=="__main__":
    n=int(input())
    ch=[0]*(n+1)
    DFS(1)

'''
    트리구조로 그려야함
    1, ch[1]=1 
    2, ch[2]=1 
    3, ch[3]=1
    4 print(i) 1, 2, 3 4 print(i)
    
    1,2 CH[3]=0
    
'''
    

