#막대기 입력
#잘리는거 세기
ip = input()
cnt = 0
stack = []
for i in range(len(ip)):
    if i=='(':
        stack.append(ip[i])
    else:
        stack.pop()
        if ip[i-1] == '(':
            cnt += len(ip)
        else:
            cnt +=1
print(cnt)
