N = int(input())

str_list = [input().strip() for _ in range(N)]

def merge(n, lst):
    if n == 0:
        return ''
    if n == 1:
        return lst[0]
    
    mid = n // 2
    str1 = merge(mid, lst[:mid])
    str2 = merge(n - mid, lst[mid:])
    