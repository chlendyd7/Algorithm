import sys
X,Y,W,S = map(int, sys.stdin.readline().split())
answer = 0
if W * 2 <= S:
    print((X+Y) * 2)
else:
    smaller = min(X, Y)
    answer = smaller * S
    absXY = abs(X-Y)
    if W > S:
        if absXY % 2 == 0:
            answer += absXY * S
        else:
            answer += (absXY-1) * S + W
    else:
        answer += absXY * W
    print(answer)
