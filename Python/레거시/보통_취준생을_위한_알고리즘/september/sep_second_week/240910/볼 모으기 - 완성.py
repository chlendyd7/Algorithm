n = int(input())
balls = input()

b_ball = min(balls.lstrip('R').count('R'), balls.rstrip('R').count('R'))
r_ball = min(balls.lstrip('B').count('B'), balls.rstrip('B').count('B'))

print(min(b_ball, r_ball))
