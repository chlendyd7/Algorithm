n=int(input())
stack = []
cnt = 0
result = []
no_message = True
for i in range(n):
    x=int(input())
    
    while cnt < x:
        cnt +=1
        stack.append(cnt)
        result.append('+')
    
    if stack[-1] == x:
        stack.pop()
        result.append('-')
    
    else:
        no_message = False
        break

        
if no_message == False:
    print('NO')
else:
    print("\n".join())