import sys
input = sys.stdin.readline
minus = 0
string = input().rstrip()
list_to_split_minus = string.split('-')
ls = []
for list in list_to_split_minus:
    list_to_split_plus = map(int, list.split('+'))
    ssum = sum(list_to_split_plus)
    ls.append(ssum)

result = ls[0]
for i in range(1, len(ls)):
    result -= ls[i]


print(result)
