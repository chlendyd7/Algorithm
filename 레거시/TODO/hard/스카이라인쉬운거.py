def solution(skylines):
    global answer
    stk = [0]
    for p in skylines:
        height = p
        while stk[-1] > p:
            if stk[-1] != height:
                answer +=1
                height = stk[-1]
            stk.pop()
        stk.append(p)


skylines = []
n = int(input())
for i in range(n):
    skylines.append(int(input().split()[1]))
skylines.append(0)
answer = 0
solution(skylines)
print(answer)
