import sys
sys.stdin=open("input.txt", "r")
def DFS(L, P):
    global cnt
    if L==n:
        cnt+=1
        for j in range(P): #알파벳 찍어주기
            print(chr(res[j]+64), end='')
        print()
    else:
        for i in range(1, 27):
            if code[L]==i: # 한자리 숫자 일 때
                res[P]=i #res p 번째는 i대입
                DFS(L+1, P+1) # p 는 index
            
            elif i>=10 and code[L]==i//10 and code[L+1]==i%10: #L은 i의 10의자리 숫자와 같아야함, L+1은 i의 1의 자리와 같아야함
                res[P]=i
                DFS(L+2, P+1) #두자리 숫자이면

if __name__=="__main__":
    code=list(map(int, input())) #들어가는 곳
    n=len(code) # 종착점
    code.insert(n, -1) #out of range index 범위 오류 방지
    res=[0]*(n+3)
    cnt=0
    DFS(0, 0)
    print(cnt)