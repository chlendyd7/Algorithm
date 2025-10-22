'''
응시자의 수는 Ai 감시 할 수 있는 응시자의 수 B
부감독관은 감시할 수 있는 응시자의 수 C
총감독관은 1명 부감독관은 여러명
모두 감시해야 한다면 필요한 감독관의 수 최소값을 구하라

시간제한 2초
'''
N = int(input())
classes = list(map(int, input().split()))
B, C = map(int, input().split())

print(classes)

result = 0
for cl in classes:
    r = 1
    r += (cl - B) / C
    if 