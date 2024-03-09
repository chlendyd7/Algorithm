n=int(input())
ls=list(map(int,input().split()))
# 앞의 공간만 신경쓰면 됨 => 0 
# 빈 공간이 어차피 큰 숫자이니까
seq=[0]*n
for i in range(n): #i가 1일 때
    for j in range(n):
        if ls[i]==0 and seq[j]==0:
            seq[j] = i+1
            break
        elif seq[j]==0:
            ls[i]-=1

print(seq, end=' ')

