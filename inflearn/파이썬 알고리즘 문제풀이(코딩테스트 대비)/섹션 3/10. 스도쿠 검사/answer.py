import sys
sys.stdin=open("input.txt", "r")
def check(a):#스도쿠는 1~9의 숫자밖에 없음 즉 중복되는 숫자가 나타나면 나머지 숫자는 등장하지 않게 됨
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1  #스도쿠의 숫자 번호를 1로 체크
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9: #체크된 모든 리스트를 더하여 9가 되면 True(1~9까지의 숫자가 나온다)
            return False 
    for i in range(3):
        for j in range(3):
            ch3=[0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1 #3칸씩 이동하면서 탐색하게 된다
            if sum(ch3)!=9:
                return False
    return True 

a=[list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")