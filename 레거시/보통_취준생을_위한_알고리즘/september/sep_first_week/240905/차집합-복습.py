a, b = map(int, input().split())

set1 = set(list(map(int,input().split())))
set2 = set(list(map(int,input().split())))

result = set1 - set2
if not result:
    print(0)
else:
    print(len(result))
    print(*sorted(list(result)))
