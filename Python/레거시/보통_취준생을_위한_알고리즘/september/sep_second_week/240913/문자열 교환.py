string = input()
cnt_a = string.count('a')
answer = float('inf')
string += string[:cnt_a]
for i in range(len(string)- cnt_a):
    cnt_b = string[i:i+cnt_a].count('b')
    answer = min(answer, cnt_b)

print(answer)
