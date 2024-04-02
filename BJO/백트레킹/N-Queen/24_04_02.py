def attack(x):
    for i in range(x):
        if row[i]==row[x]:
            return True
        if abs(row[i]-row[x])==abs(i-x):
            return True
    return False


def dfs(start):
    global cnt
    if start==n:
        cnt+=1
    



n = int(input())
row = [0]*n
cnt = 0
dfs(0)
print(cnt)