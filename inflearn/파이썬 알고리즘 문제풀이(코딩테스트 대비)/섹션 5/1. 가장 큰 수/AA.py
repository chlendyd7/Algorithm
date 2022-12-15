num, m=map(int, input().split())
<<<<<<< Updated upstream
num=list(map(int, str(num)))#이렇게 해주는 이유?
stack=[]
for x in num:
    while stack and m>0 and stack[-1]<x: # stack 비어있으면 거짓, m>0
        stack.pop()# stack[-1]:마지막에 들어간 숫자가
        m-=1# x:현재의 m 보다 작으면 끄집어냄 while문을 끝낼 시 자기보다 작은 숫자들 다 제거
    stack.append(x)
if m!=0:
    stack=stack[:-m] #-m의 전것을 지움 ex)[1:4] 1~3까지
res=''.join(map(str, stack))
print(res)

# 정리: 첫번째 while문이 돌 때에는 stack이 빈 list라 넘어가게 됨
# 계속해서 num을 돌려야 하기 때문에 stack[-1]이 < 현재의 list의 값과 비교
# for 문 다 돌았는데도 m이 남아 있을 시 뒷자리부터 제거하기 때문에 [:-m]으로 슬라이싱
=======
num=list(map(int, str(num)))
stack=[]
for x in num:
    while stack and m>0 and stack[-1]<x: #stack의 list안에 값이 있으면 참을 리턴
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
res=''.join(map(str, stack))
print(res)





>>>>>>> Stashed changes
