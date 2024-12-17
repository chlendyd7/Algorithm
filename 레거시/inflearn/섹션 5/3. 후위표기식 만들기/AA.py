m = input() # 중위식을 담음
stack = [] # 
res = ''
for x in m:
    if x.isdecimal(): # x가 10진수 숫자면 참
        res += x # res 에 숫자 누적
    else:
        if x =='(': 
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1]!='(':
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()
print(res)

# 컴퓨터는 연산우선자를 먼저 처리하는 것이 빠르다
# 질문: _로 받는 것 각각 int 인가? 전부 str임
# isdecimal() Return True if the string is a decimal(소수) string, False otherwise.
