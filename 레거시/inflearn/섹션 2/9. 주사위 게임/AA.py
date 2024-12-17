<<<<<<< HEAD
tmp = input().split()
tmp.sort()
a, b, c = map(int, tmp)
=======
n = int(input())
tmp = 0
for i in range(n):
    num=0
    
    a, b, c = map(int, input().split())
    
    if a == b == c:
        num = 10000+ a*1000
    elif a == b or b == c:
        num = 1000 + b*100
    elif c==a:
        num = 1000 + a*100
    else:
        num = max(a,b,c)*100
    
    if tmp < num:
        tmp = num

print(tmp)



        
        
>>>>>>> 44699fea016ce63ea86aa880ba2977ef38a90525
