'''
    list에 담고 같으면 pop
    마지막 하나
'''

n=int(input())
ls = []
for _ in range(n):
    ls.append(input())
for _ in range(n-1):
    word = input()
    i = len(ls) - 1
    while i >= 0:
        if word == ls[i]:
            ls.pop(i)
        i -= 1
print(ls[0])