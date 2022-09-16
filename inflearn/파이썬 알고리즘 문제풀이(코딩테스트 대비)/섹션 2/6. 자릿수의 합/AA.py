from re import X


n=int(input())
a = list(map(int, input().split()))
max =0

def digit_sum(x):
    sum=0
    for i in str(x):
        sum += int(i)
    return sum

for i in a:
    tot = digit_sum(i)
    if tot > max:
        max = tot
        res = i
print(res)
    