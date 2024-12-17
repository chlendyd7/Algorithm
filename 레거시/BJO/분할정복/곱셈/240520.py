import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())

def multiple(a,n):
    next = n//2
    if n==1:
        return a%c
    else:
        temp = multiple(a,next)
        if n%2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c

print(multiple(a,b))
