tmp = int(input())
score = list(map(int, input().split()))
output = 0
count = 0
for i in score:
    if i == 1:
        count +=1
        output += count
    else:
        count =0

print(output)

