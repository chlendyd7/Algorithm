# https://www.acmicpc.net/problem/1541

string = input().split('-')
answer = 0

for i in string[0].split('+'):
    answer += int(i)

for j in string[1:]:
    for k in j.split('+'):
        answer -= int(k)

print(answer)
