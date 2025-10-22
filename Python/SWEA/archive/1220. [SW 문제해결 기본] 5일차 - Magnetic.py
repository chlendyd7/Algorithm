'''
return: 테이블 위에 남아있는 교착 상태의 개수를 구하라
A는 S에 이끌리면서 테이블 아래로 떨어짐
B는 N에 이끌리면서 테이블 아래로 떨어진다
나머지 자성체들은 서로 충돌, 교착 상태에 빠져 움직이지 않게 된다

반대 방향으로 움직이는게 하나라도 있으면 교착상태로 움직이지 않는다
셋 이상의 자성체들이 서로 붙어있을 경우 하나의 교착상태

## input이 0, 1, 2로 들어옴
100 x 100의 크기
윗쪽 N 아랫 부분 S극
1은 아래로 2는 위로
'''

def solution():
    _ = input()
    board = [list(map(int, input().split())) for _ in range(100)]

    cnt = 0
    for col in range(100):
        check = 0
        for row in range(100):
            if board[row][col] == 1:
                check = 1
            elif board[row][col] == 2:
                if check == 1:
                    cnt += 1
                check = 0

    return cnt

for t in range(1, 11):
    print(f'#{t} {solution()}')

'''
    [1,2,2,1]
    check = 1
    
    cnt += 1
    check = 2
    
    check = 2
    cnt += 1
    check = 1
'''

'''
놓친 부분
반례 [2, 1]을 생각 -> 둘은 마주치지 않고 밑으로 떨어짐
'''
