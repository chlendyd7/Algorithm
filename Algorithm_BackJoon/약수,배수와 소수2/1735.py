import math
import sys
input = sys.stdin.readline

bunsu1 = list(map(int,input().split()))
bunsu2 = list(map(int,input().split()))

e,f = (bunsu1[0] * bunsu2[1]) + (bunsu2[0] * bunsu1[1]) , bunsu2[1]*bunsu1[1]
gcd = math.gcd(e,f)
if gcd != 1:
    e//=gcd
    f//=gcd
print(e,f)


# print(bunsu1,bunsu2)

