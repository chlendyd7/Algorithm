n = int(input())
for i in range(1, n+1):
    num = sum(map(int,str(i)))
    num_r = num + i
    if num_r == n:
        print(i)
        break
    elif i == n:
        print(0)