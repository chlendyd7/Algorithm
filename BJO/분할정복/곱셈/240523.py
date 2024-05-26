import sys
input = sys.stdin.readline
a,b,c = list(map(int,input().split()))

def multiple(a,b):
    next = b//2
    if b == 1:
        return a%c
    else:
        temp = multiple(a,next)
        if b%2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c

print(multiple(a,b))
s