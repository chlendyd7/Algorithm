n=int(input())
drink = [0]*10001
for i in range(1,n+1):
    drink[i]=(int(input()))

dy=[0]*10001
dy[1] = drink[1]
dy[2] = drink[1] + drink[2]
dy[3] = max(drink[3]+drink[1], drink[3]+drink[2], dy[2])
for i in range(4, n+1):
    dy[i] = max(dy[i-3]+ drink[i-1]+drink[i], dy[i-2]+drink[i], dy[i-1])

print(max(dy))
