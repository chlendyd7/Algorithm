# n = "00120"
# n = int(n)
# print(n)
# # int화 하면 알아서 00없어짐
# isdecimal string이 숫자인지 True,False return

n = input()
out = ""
for i in n:
    if i.isdecimal():
        out+=i
out = int(out)

# 약수 만들기
cnt=0
for i in range(1, out+1):
    if out % i == 0:
        cnt+=1
print(out)
print(cnt)