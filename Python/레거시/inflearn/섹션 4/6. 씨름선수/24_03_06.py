n = int(input())
meeting = []
for i in range(n):
    s, e=map(int, input().split())
    meeting.append((s,e))

meeting.sort(reverse=True)
cnt = 0
largest = 0
for x,y in meeting:
    if x>largest:
        if 
    