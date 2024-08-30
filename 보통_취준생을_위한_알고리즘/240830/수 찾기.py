def binary_search(target):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if nlst[mid] == target:
            return 1
        else:
            if nlst[mid]<=target:
                start=mid+1
            else:
                end = mid -1
    return 0

n = int(input())
nlst = list(map(int,input().split()))
nlst.sort()

m = int(input())
mlist = list(map(int,input().split()))

for i in range(m):
    print(binary_search(mlist[i]))
