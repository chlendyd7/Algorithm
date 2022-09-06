T = int(input())
l = []
for i in range(T):
    h,w,n = map(int, input().split())
    w=0
    if n % h ==0:
        print(h*100 + n//h)
    else:
        while n > h:
            n = n - h
            w += 1
        print(f'{n*100+w+1}')
    
