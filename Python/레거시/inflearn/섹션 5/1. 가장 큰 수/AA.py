'''
    선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하
    여 가장 큰 수를 만들라고 했습니다. 여러분이 현수를 도와주세요.(단 숫자의 순서는
    유지해야 합니다)
    만약 5276823 이 주어지고 3개의 자릿수를 제거한다면
    7823이 가장 큰 숫자가 됩니다.
    1. 빈 stack 만들기
    2. 넣기
    3. 비교하기 들어가려는 값이 더 크면
    4. 빼기(m개)
    5. m가 남아있으면 m개 만큼 버리기
    6. ex) 987654 [:-m]

'''
num,m=map(int,input().split())
num = list(map(int, str(num)))
stack=[]
for x in num:
    while stack and m>0 and x>stack[-1]:
        stack.pop()
        m-=1
    stack.append(x)

if m !=0:
    stack = stack[:-m]
res=''.join(map(str, stack))
print(res)





















# num, m=map(int, input().split())
# num=list(map(int, str(num)))
# stack=[]
# for x in num:
#     while stack and m>0 and stack[-1]<x: #stack의 list안에 값이 있으면 참을 리턴
#         stack.pop()
#         m-=1
#     stack.append(x)
# if m!=0:
#     stack=stack[:-m]
# res=''.join(map(str, stack))
# print(res)
# '''
# 7823 
# '''