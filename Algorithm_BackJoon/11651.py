n = int(input())
location = [list(map(int,input().split())) for _ in range(n)]
location.sort(key=lambda x:(x[1],x[0]))

for x,y in location:
    print(x,y)
