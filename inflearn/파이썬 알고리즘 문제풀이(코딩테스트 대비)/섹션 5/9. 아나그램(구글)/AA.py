first = input()
second = input()
p1=dict()
p2=dict()
# for i in first:
#     p1[i] +=1 #key 값이 생성되있지 않기 때문에 key error
for i in first:
    p1[i] = p1.get(i,0)+1


for i in second:
    p2[i]=p2.get(i,0)+1

for i in p1.keys():
    if i in p2.keys():
        if p1[i] != p2[i]:
            print("NO")
            break
    else:
        print("NO")
else:
    print("YES")

# # dict.get()
# get함수는 선언된 dict에서 출력하고자 하는 key가 있으면, 그에 해당하는 value를 출력해줍니다.
# 또한, 출력하고자 하는 key가 없으면, 오류가 아닌 None을 출력합니다.

a = input()
b = input()
sH = dict() #string hash
for x in a:
    sH[x]=sH.get(x,0)+1

for x in b:
    sH[x] = sH.get(x,0)-1

for x in a: #다시 하여금 접근
    if sH.get(x)>0:
        print("NO")
        break
    else:
        print("YES")

# # 리스트 해쉬 아스키 넘버를 이용
# a = input()
# b = input()
# str1 = [0]*52
# str2 = [0]*52
# for x in a:
#     if x.isupper(): #대문자 이면 True return
#         str1[ord(x)-65]+=1 # ord() 문자를 아스키넘버로 변환 대문자는 65~90, 소문자는 97~122 26개씩
#     else:
#         str1[ord(x)-71]+=1
# for x in b:
#     if x.isupper():
#         str2[ord(x)-65]+=1
#     else:
#         str2[ord(x)-71]+=1
# # if str1==str2: 이렇게 해도 됨
# for i in range(52):
#     if str1[i] != str2[i]:
#         print("NO")
#         break
#     else:
#         print("YES")
