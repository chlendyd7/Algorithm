n=int(input())
drink = []
for _ in range(n):
    drink.append(int(input()))
dy=[0]*10001
drink.insert(0,0)
dy[1] = drink[1]
dy[2] = drink[1]+drink[2]
dy[3] = max(drink[3]+drink[1], drink[3]+drink[2], dy[2])

for i in range(4, n+1):
    dy[i] = max(dy[i-3]+drink[i]+drink[i-1], drink[i]+dy[i-2], dy[i-1])
print(drink)
print(max(dy))