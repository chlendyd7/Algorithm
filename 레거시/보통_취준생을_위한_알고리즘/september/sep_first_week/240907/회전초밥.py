n,d,k,c = map(int,input().split())
dish = [int(input()) for _ in range(n)]
mx_num = 0
for i in range(n):
    if i+k > n:
        num = len(set(dish[i:n] + dish[:(i+k)%n] + [c]) )
    else:
        num = len(set(dish[i:i+k] + [c]))
    mx_num = max(mx_num, num)
print(mx_num)
