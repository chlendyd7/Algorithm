import sys
input = sys.stdin.readline

장대 = int(input())
횟수 = 0
sb = []

def hanoi(n, f, t, oth):
    if n==0:
        return
    else:
        횟수 +=1
        hanoi(n-1, f, oth, t)
        sb.append(n-1, f + " " + t + '\n')
        hanoi(n-1, oth, t, f)
