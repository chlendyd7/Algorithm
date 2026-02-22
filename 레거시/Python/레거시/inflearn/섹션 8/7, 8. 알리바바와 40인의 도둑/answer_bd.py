import sys
sys.stdin = open("input.txt", 'r')    
if __name__=="__main__":
    n=int(input())
    arr=[list(map(int, input().split())) for _ in range(n)]
    dy=[[0]*n for _ in range(n)]
    dy[0][0]=arr[0][0]
    for i in range(1, n):
        dy[0][i]=dy[0][i-1]+arr[0][i] # 가로 세로의 값 경로 1가지 경우 밖에 없으니 초기화
        dy[i][0]=dy[i-1][0]+arr[i][0] # 모든 dy을 채워줌?
    for i in range(1, n):
        for j in range(1, n):
            dy[i][j]=min(dy[i-1][j], dy[i][j-1])+arr[i][j] #아래 1 오른쪽 1 움직이면서 작은 곳으로 이동 
    print(dy[n-1][n-1]) 
    