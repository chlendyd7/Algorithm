n=int(input())
dic = dict()
for i in range(n):
    dic[input()]=1
print(dic)

for i in range(n-1):
    dic[input()]=0

for key, val in dic.items():
    if val==1:
        print(key)