first_string = input()
second_string = input()
h,w = len(first_string), len(second_string)
cache = [[0]*(w+1) for _ in range(h+1)]

for i in range(1, h+1):
    for j in range(1, w+1):
        if first_string[i-1] == second_string[j-1]:
            cache[i][j] = cache[i-1][j-1]+1
        else:
            cache[i][j] = max(cache[i][j-1], cache[i-1][j])
print(cache[-1][-1])