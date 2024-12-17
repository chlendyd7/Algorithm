string = input()
cnt_a = string.count('a')
string +=  string[:cnt_a]
answer = 10000
for i in range((len(string) - cnt_a)):
    slicing_string = string[i:i+cnt_a]
    cnt_b = slicing_string.count('b')
    answer = min(answer, cnt_b)
print(answer)
