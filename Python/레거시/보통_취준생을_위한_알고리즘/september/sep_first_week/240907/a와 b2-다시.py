import sys
def dfs(string):
    if string == t:
        print(1)
        sys.exit()

    if len(string) == 0:
        return 0
    if t[-1] == 'A':
        dfs(string[:-1])
    if t[0] == 'B':
        dfs(string[1:][::-1])

s = input()
t = input()
