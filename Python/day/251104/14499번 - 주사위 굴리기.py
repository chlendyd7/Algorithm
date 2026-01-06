N,M,x,y,K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

def roll(direction):
    top, bottom, north, south, west, east = dice
    
    if direction == 1:
        dice[0], dice[1], dice[4], dice[5] = west, east, bottom, to[]