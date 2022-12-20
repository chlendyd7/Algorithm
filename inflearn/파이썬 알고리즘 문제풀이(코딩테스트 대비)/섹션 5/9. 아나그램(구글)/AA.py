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