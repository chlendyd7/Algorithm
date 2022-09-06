a,b,v = map(int, input().split())
d = 0#day
h = 0#height
while True:
    d+=1
    h+=a
    if h>=v:
        break
    else:
        h-=b
print(d)