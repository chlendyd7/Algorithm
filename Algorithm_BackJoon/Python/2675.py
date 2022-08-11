N = input()
for i in range(N):
    num, s = input().split()
    text = ""
    for j in s:
        text += int(num) * s
    print(text)
    