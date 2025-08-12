T = int(input())
for tc in range(1, 1+T):
    arr = input()
     
    stack = [0]*len(arr)
    top = -1
    error = 0
     
    for i in arr:
        if i == "{" or i == "(":
           top += 1
           stack[top] = i
        
        elif i == "}":
            if stack[top] == "{":
                top -= 1
            else:
                error = 1
                break
             
        elif i == ")":
            if stack[top] == "(":
                top -= 1
            else:
                error = 1
                break
             
    if error ==0 and top == -1:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
        