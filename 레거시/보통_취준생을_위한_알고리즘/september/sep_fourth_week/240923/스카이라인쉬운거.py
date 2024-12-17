def solution(skylines):
    global answer
    stk = [0]
    for p in skylines:
        height = p
        while stk[-1] < p:
            answer += 1
            height = stk[-1]
            stk.pop()
        stk.append(p)        


n = int(input())
answer = 0
sky_lines = []
for _ in range(n):
    x,y = map(int,input().split())
    sky_lines.append(y)
