# https://www.acmicpc.net/problem/1914
def hanoi(num, start, temp, end):
    if num == 1:
        print(start, end)
    else:
        hanoi(num-1, start, end, temp)
        print(start, end)
        hanoi(num-1, temp, start, end)


n = int(input())
print(2**n - 1)
if(n<= 20):
    hanoi(n, 1, 2, 3)
