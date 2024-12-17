def lis(lst):
    lis = []
    for l in lst:
        if not lis or lis[-1] < l:
            lis.append(l)
        else:
            start = 0
            end = len(lis)
            while start <= end:
                mid = (start + end) // 2
                if l > lis[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            lis[start] = l

n = int(input())
boxs = list(map(int, input().split()))
print(lis(boxs))