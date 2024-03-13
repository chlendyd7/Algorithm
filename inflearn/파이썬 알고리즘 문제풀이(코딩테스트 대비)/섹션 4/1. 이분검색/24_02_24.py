n,m= map(int, input().split())
ls = list(map(int,input().split()))
ls.sort()
print(ls)
def salt(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return salt(array, target, start, mid - 1)
    else:
        return salt(array, target, mid + 1, end)


print(len(ls))
print(salt(ls, m, 0, n-1))