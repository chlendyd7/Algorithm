def solve(x, y, startX, startY, ballX, ballY):
    dists = []
    # 위쪽 벽
    # 단, x좌표가 같고 목표의 y가 더 크면 안된다.
    if not (ballX == startX and ballY > startY):
        d2 = (ballX - startX)**2 + (ballY - 2*y+startY)**2
        dists.append(d2)
    # 아래쪽 벽
    # 단, x좌표가 같고 목표의 y가 더 작으면 안된다.
    if not (ballX == startX and ballY < startY):
        d2 = (ballX - startX)**2 + (ballY + startY)**2
        dists.append(d2)
    # 왼쪽 벽에 맞는 경우
    # 단, y좌표가 같고 목표의 x가 더 작으면 안된다.
    if not (ballY == startY and ballX < startX):
        d2 = (ballX + startX)**2 + (ballY - startY)**2
        dists.append(d2)
    # 오른쪽 벽
    # 단, y좌표가 같고 목표의 x가 더 크면 안된다.
    if not (ballY == startY and ballX > startX):
        d2 = (ballX - 2*x+startX)**2 + (ballY - startY)**2
        dists.append(d2)
    
    return min(dists)
    
def solution(m, n, startX, startY, balls):
    answer = []
    for ballX, ballY in balls:
        answer.append(solve(m, n, startX, startY, ballX, ballY))
    return answer


def solve(x, y, startX, startY, ballX, ballY):
    # 벽을 고려한 반사 좌표 계산
    reflections = [
        (ballX, -ballY),         # 아래쪽 벽 반사
        (ballX, 2*y - ballY),    # 위쪽 벽 반사
        (-ballX, ballY),         # 왼쪽 벽 반사
        (2*x - ballX, ballY)     # 오른쪽 벽 반사
    ]
    
    # 조건에 따라 유효한 반사만 선택
    dists = []
    for rx, ry in reflections:
        if not (rx == startX and ry == startY):  # 출발점을 지나가는 반사는 제외
            d2 = (rx - startX)**2 + (ry - startY)**2
            dists.append(d2)
    
    return min(dists)

def solution(m, n, startX, startY, balls):
    return [solve(m, n, startX, startY, ballX, ballY) for ballX, ballY in balls]
