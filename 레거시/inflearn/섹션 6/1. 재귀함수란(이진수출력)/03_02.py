
def DFS(n):
    if n==0:
        return
    else:
        DFS(n//2)
        print(n%2,end='')



if __name__ == "__main__":
    n = int(input())
    DFS(n)
