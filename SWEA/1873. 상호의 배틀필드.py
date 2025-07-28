'''

전차가 포탄을 발사하면, 포탄은 벽돌로 만들어진 벽 또는 강철로 만들어진 벽에 충돌하거나 게임 맵 밖으로 나갈 때까지 직진한다.
만약 포탄이 벽에 부딪히면 포탄은 소멸하고 부딪힌 벽이 벽돌로 만들어진 벽이라면 이 벽은 파괴되어 칸은 평지가 된다.
강철로 만들어진 벽에 포탄이 부딪히면 아무 일도 일어나지 않는다.
게임 맵 밖으로 포탄이 나가면 아무런 일도 일어나지 않는다.
초기 게임 맵의 상태와 사용자가 넣을 입력이 순서대로 주어질 때, 모든 입력을 처리하고 나면 
게임 맵의 상태가 어떻게 되는지 구하는 프로그램을 작성하라.
'''

direction = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

def solution():
    H, W = map(int, input().split())
    board = []
    direction_map = {'^': 'U', 'v': 'D', '<': 'L', '>': 'R'}
    for _ in range(H):
        board.append(list(input()))
    for i in range(H):
        for j in range(W):
            if board[i][j] in direction_map:
                way = direction_map[board[i][j]]
                break
        else:
            continue
        break

    N = int(input())
    cmd = list(input())
    for c in cmd:
        if c == 'S':
            
    
    return


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')