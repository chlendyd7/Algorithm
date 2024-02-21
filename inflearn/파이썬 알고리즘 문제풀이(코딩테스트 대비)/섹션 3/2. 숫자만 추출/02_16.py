# n = input()
# ascii_codes = [ord(char) for char in n]
# ls = []
# for i in ascii_codes:
#     if i >=48 or i<=57:
#         ls.append(i) 

# numbers = [int(chr(code)) for code in ascii_codes]
# result_number = int(''.join(map(str, numbers)))

# print(ls)

import math


n=input()
out=""
for i in n:
    if i.isdecimal():
        out+=i
out=int(out)

sqrt_out = int(math.sqrt(out))
cnt = 0
for i in range(1, sqrt_out+1):
    if out % i == 0:
        cnt += 1
        if i != out //i:
            cnt +=1

print(out)
print(cnt)