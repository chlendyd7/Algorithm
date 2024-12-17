'''
    나눠야됨
'''
k,n = map(int,input().split())
line_ls = []
for _ in range(k):
    line_ls.append(int(input()))

start = 1
end = max(line_ls)
answer = 0

while start <= end:
    mid = (start + end) // 2
    num = 0
    for line in line_ls:
        num += line//mid
    if num >= n:
        start = mid + 1
        answer = max(mid, answer)
    else:
        end = mid - 1

print(answer)