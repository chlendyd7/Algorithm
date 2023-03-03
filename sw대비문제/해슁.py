n = int(input())
a = list(input())
result = 0
for i in range(n):
    result += ((ord(a[i])-96)*31**i)%1234567891
print(result%1234567891)

l = int(input())
data = list(input())
sum = 0
for i in range(l):
    sum = sum + (ord(data[i]) % 96)*(31**i)
print(sum % 1234567891)