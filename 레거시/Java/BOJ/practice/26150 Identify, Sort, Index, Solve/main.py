N = int(input())
lst = []
for _ in range(N):
    title, num, dif = input().split(" ")
    lst.append((title, int(num), int(dif)))

lst.sort(key=lambda x:x[1])
result = ''
for title, num, dif in lst:
    result += title[dif-1].upper()
print(result)


