n = int(input())
balls = input()
A_strip_balls = min(balls.rstrip('R').count('R'), balls.lstrip('R').count('R'))
B_strip_balls = min(balls.rstrip('B').count('B'), balls.lstrip('B').count('B'))

print(min(A_strip_balls, B_strip_balls))
