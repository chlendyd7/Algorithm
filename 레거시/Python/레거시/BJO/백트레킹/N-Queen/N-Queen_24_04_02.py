
def attack(x):
    for i in range(x):
        if row[x]==row[i]:
            return True
        if abs(row[x]-row[i]) == abs(x-i):
            return True
    return False


def dfs(start):
    global cnt
    if start==n:
        cnt+=1
    else:
        for i in range(n):
            row[start]=i
            if not attack(start):
                dfs(start+1)

n=int(input())
row=[-1]*n
cnt=0
dfs(0)
print(cnt)