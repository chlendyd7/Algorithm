n = int(input())
boxs = list(map(int, input().split()))
lis = []

for box in boxs:
    if not lis or lis[-1] < box:
        lis.append(box)
    else:
        start = 0
        end = len(lis) - 1
        while start <= end:
            mid = (start+end) // 2
            if lis[mid] < box:
                start = mid + 1
            else:
                end = mid - 1
        lis[start] = box

print(len(lis))
