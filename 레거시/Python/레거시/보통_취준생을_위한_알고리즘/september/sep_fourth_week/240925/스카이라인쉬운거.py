def solution(skylines):
    global answer
    stk = [0]
    for p in skylines:
        height = p
        while stk[-1] > p:
            if stk[-1] != height:
                answer += 1
                height = stk[-1]
            stk.pop()
        stk.append(p)

n = int(input())
skylines = [list(map(int,input().split()[1])) for _ in range(n)]
skylines.append(0)
answer = 0