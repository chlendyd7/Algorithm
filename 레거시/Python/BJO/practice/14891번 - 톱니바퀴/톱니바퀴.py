'''
톱니바퀴
N극 S극 하나 가짐
1, 2, 3, 4
K번 회전: 시계방향, 반 시계방향

옆도 회전 가능

맞닿은 극이 다르면 반대 방향으로 회전

극이 같으면 회전x 다르면 회전

점수의 합을 구하라

시계방향 순서

다섯 번째

스택 사용 pop.append하기
'''
N = 0
S = 1

wheel1 = input()
wheel2 = input()
wheel3 = input()
wheel4 = input()
K = int(input())

def simulation(wheel, d):
    # 오른쪽
    for i in range(wheel, 4):
        
    # 왼쪽
    for i in range(wheel, -1, -1):


for _ in range(K):
    w, d = map(int, input().split())
    
print(wheel4)
