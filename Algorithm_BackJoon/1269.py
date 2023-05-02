import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

count = len(A-B) + len(B-A)
#문제 나온대로 연산하면 된다 list
print(count)
