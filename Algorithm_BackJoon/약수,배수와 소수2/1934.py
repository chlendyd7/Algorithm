#유클리드 호제법, 최대공약수를 구하고 최대 공약수를 이용하여 최소 공배수를 구한다
#x,y = y,x % y 최대 공약수
#최소 공배수 x*y//최대 공약수
import sys
input = sys.stdin.readline

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def lcm(x,y):
    result = (x*y) // gcd(x,y)
    return result


T = int(input())

for i in range(T):
    x,y = map(int,input().split())
    print(lcm(x,y))
