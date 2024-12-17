first_string = input()
second_string = input()
h,w = len(first_string), len(second_string)
dy = [[0]*(w+1) for _ in range(h+1)]
for i in range(1, h+1):
    for j in range(1, w+1):
        if first_string[i-1] == second_string[j-1]:
            dy[i][j] = dy[i-1][j-1]+1
        else:
            dy[i][j] = max(dy[i-1][j], dy[i][j-1])
print(dy[-1][-1])