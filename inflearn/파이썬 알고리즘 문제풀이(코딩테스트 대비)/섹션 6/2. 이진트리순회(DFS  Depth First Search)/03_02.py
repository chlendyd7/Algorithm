def DFS(n):
    if n>7:
        return
    else:
        print(n, end='')
        DFS(n*2)
        DFS(n*2+1)







if __name__ == "__main__":
    # m=int(input())
    DFS(1)
    
