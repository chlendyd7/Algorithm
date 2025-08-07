#for tc in range(1, 11):
N = int(input())
data = [list(map(int, input().split())) for _ in range(100)]


#끝나는 지점이 2인 좌표 찾기(여기서 시작)
for j in range(100):
    if data[99][j] == 2:
        fin = j

#아래서부터 이어지게 올라가기
for i in range(99, 0, -1):
    if data[i][fin-1] == 1:
        while data[i][fin] == 1:
            fin += 1
    elif data[i][fin+1] == 1:
        while data[i][fin] == 1:
            fin -= 1
    
print(i)
