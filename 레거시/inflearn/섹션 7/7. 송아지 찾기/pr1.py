from collections import deque


MAX = 10000
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
n,m = map(int, input().split())
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)
while dQ:
    


#아이폰 동영상 가운데 잘라내기
def DFS(S,E):
    global cnt
    if S==e:
        if cnt>E:
            cnt = E
    
    
    if e>S+5:
        DFS(S+5, E+1)
    
    else:
        DFS(S+1, E+1)
    

    






if __name__ == "__main__":
    s,e = map(int,input().split())
    cnt = 0
    DFS(s,0)
    print(cnt)