string = input()
answer = float('inf')
a_cnt = string.count('a')

string += string[:a_cnt - 1]
for i in range(len(string) - (a_cnt - 1)):
    slice_string = string[i:i+a_cnt]
    b_count = slice_string.count('b')
    answer = min(answer, b_count)

print(answer)