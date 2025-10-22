'''
    1. 자기자리 찾은 경우
    2. 자기자리 못찾은 경우
'''
import sys
# sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
seq=[0]*n
for i in range(n):
    for j in range(n):
        if(a[i]==0 and seq[j]==0): # j는 그곳에 숫자가 있으면 안됨
            seq[j]=i+1 # i는 1부터 시작
            break # j break
        elif seq[j]==0:
            a[i]-=1

for x in seq:
    print(x, end=' ')