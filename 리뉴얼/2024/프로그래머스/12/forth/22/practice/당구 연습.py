def solve(x, y, startX, startY, ballX, ballY):
    dists = []

    if not (ballX == startX and ballY > startY):
        d2 = (ballX - startX)**2 + (ballY - 2 * y + startY) ** 2
        dists.append(d2)
    if not (ballX == startX and ballY < startX):
        d2 = (ballX - startX)