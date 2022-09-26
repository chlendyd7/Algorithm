import sys

sys.stdin = open("input.txt","r")

n,k = map(int,input().split())
a = list(map(int, input().split()))
res = set()
for i in range(n):
    for j in range(i+1, n):#와이?
        
