n, limit = map(int, input().split())  # Number of towns, truck capacity
m = int(input())  # Number of deliveries
arr = [list(map(int, input().split())) for i in range(m)]  # Delivery info
trucks = [limit for i in range(n+1)]  # Truck capacity for each segment
arr.sort(key=lambda x: x[1])  # Sort deliveries by destination
print(arr)
result = 0
for i in arr:
    min_box = limit
    for j in range(i[0], i[1]):  # Find minimum space in the truck for the route
        min_box = min(min_box, trucks[j])
    min_box = min(min_box, i[2])  # Consider the actual number of packages
    for j in range(i[0], i[1]):
        trucks[j] -= min_box  # Update truck capacity
    result += min_box  # Add delivered packages
    print(trucks, result)
print(result)
