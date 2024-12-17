l = int(input())
warehouse = list(map(int,input().split()))
m = int(input())

warehouse.sort()

for _ in range(m):
    warehouse[0] += 1
    warehouse[-1] -=1
    warehouse.sort()

print(warehouse[-1]-warehouse[0])

