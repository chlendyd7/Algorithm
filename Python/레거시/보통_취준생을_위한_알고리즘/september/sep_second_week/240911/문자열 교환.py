string = input()
answer = float('inf')
check_a = string.count('a')
string += string[:check_a - 1]
for i in range(len(string) - (check_a - 1)):
    slicing_string = string[i:i+check_a]
    check_b = slicing_string.count('b')
    answer = min(answer, check_b)

print(answer)
