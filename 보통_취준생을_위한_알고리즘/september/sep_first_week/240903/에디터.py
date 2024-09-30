string = input()
stack = [s for s in string]
m = int(input())

command_lst = []
for _ in range(m):
    command_lst.append(input().split())

cursor = len(string)
for i in range(m):
    if command_lst[i][0] == 'L':
        if not cursor == 0:
            cursor -= 1
    if command_lst[i][0] == 'D':
        if not cursor == len(stack):
            cursor += 1
    if command_lst[i][0] == 'B':
        if not cursor == 0:
            stack.pop(cursor-1)
            cursor -= 1
    if command_lst[i][0] == 'P':
        stack.insert(cursor, command_lst[i][1])
        cursor += 1
for i in stack:
    print(i, end='')
