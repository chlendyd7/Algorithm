'''
    후위표기식 만들기
    중위표기식이 입력되면 후위표기식으로 변환하는 프로그램을 작성하세요.
    중위표기식은 우리가 흔히 쓰은 표현식입니다. 즉 3+5 와 같이 연산자가 피연산자 사이에 있
    으면 중위표기식입니다.
    후위표기식은 35+ 와 같이 연산자가 피연산자 뒤에 있는 표기식입니다.
    예를 들어 중위표기식이 3+5*2 를 후위표기식으로 표현하면 352*+ 로 표현됩니다.
    만약 다음과 같이 연산 최우선인 괄호가 표현된 식이라면
    (3+5)*2 이면 35+2* 로 바꾸어야 합니다.
    ※후위 표기식이 이해가 안되면 구글링으로 공부해보는 것도 좋습니다.
    ▣ 입력설명
    첫 줄에 중위표기식이 주어진다. 길이는 100을 넘지 않는다.
    식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.
    ▣ 출력설명
    후위표기식을 출력한다.
    ▣ 입력예제 1
    3+5*2/(7-2)
    ▣ 출력예제 13+5*2/(7-2)3+5*2/(7-2)
    352*72-/+
    ▣ 입력예제 2
    3*(5+2)-9
    ▣ 출력예제 2
    352+*9-
'''

m = input() # 중위식을 담음
stack = [] # 
res = []
switch=False
for i in range(len(m)):
    print(res)
    if m[i] == '(':
        switch=True
        i+=1
    elif m[i] == ')':
        switch=False
        i+=1
    elif m[i]=='*' or m[i]=='/':
        res+=m[i+1]
        res+=m[i]
        i+=1
    elif m[i]=='+' or m[i]=='-':
        if switch:
            res+=m[i+1]
            res+=m[i]
            i+=1
        else:
            stack.append(m[i])
    if m[i].isdecimal():
        res+=m[i]

print(stack)
# for x in m:
#     if x == '(':
#         switch=True
#     elif x == ')':
#         switch=False
#     elif x=='*' or x=='/':
#         pass
#     elif x=='+' or x=='-':
#         stack.append(x)
#     else:
#         res+=x