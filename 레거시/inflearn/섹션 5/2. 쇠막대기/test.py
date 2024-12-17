s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:
        if s[i-1]=='(':
            cnt += len(stack)
        else:
            cnt += 1

