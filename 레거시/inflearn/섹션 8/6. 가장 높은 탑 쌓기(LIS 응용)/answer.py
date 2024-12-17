import sys
#sys.stdin = open("input.txt", 'r')    
if __name__=="__main__":
    n=int(input())
    bricks=[]
    for i in range(n): #하나씩 받아주기
        a, b, c=map(int, input().split())
        bricks.append((a, b, c)) # 튜플 형태로 다 넣음
    bricks.sort(reverse=True) # sort why? 내림 차순으로 sort, 튜플의 첫 번째 자료(밑면)로 sort
    dy=[0]*n # 높이만 모으면 됨
    dy[0]=bricks[0][1] # 0번 벽돌 높이 dynamic 수집
    res=bricks[0][1] 
    for i in range(1, n): # i가 가장 상단의 값?
        max_h=0 
        for j in range(i-1, -1, -1): # 왜 -1 까지? i 번째 밑의 벽돌 찾기
            if bricks[j][2]>bricks[i][2] and dy[j]>max_h  : # 밑에 벽돌 찾는중 무게가 더 커야함
                max_h=dy[j]
        dy[i]=max_h+bricks[i][1]
        res=max(res, dy[i])
    print(res)