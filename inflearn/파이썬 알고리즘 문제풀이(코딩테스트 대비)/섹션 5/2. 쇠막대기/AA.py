s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else: # )가 들어온다면 
        stack.pop()
        if s[i-1]=='(': # 레이저 빔~
            cnt += len(stack)
        else: # 앞자리가 )이다
            cnt += 1
print(cnt)


# 질문: 쇠막대기는 어디서 표현되는가? ()는 레이저, (((는 쇠막대기 갯수 )시 앞에 (가 없으면 쇠막대기 닫는 괄호
