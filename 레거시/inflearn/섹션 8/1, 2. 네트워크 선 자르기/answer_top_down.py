# DFS(7)호출 > 방법의 수 return 불필요한 그래프 뻣기 방지: 메모리제이션


def DFS(len):
    #가지 컷
    if dy[len]>0: # 기록되있는 값이 있으면
        return dy[len] # 바로 리턴해라
    if len==1 or len==2:
        return len
    else:
        dy[len]=DFS(len-1)+DFS(len-2) # 기록 테이블을 이용
        return dy[len]


if __name__=="__main__":
    n=int(input())
    dy=[0]*(n+1)
    print(DFS(n))