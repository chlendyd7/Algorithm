n = int(input())
meeting = []
for i in range(n):
    a, b = map(int,input().split())
    meeting.append((a,b))
meeting.sort(key=lambda x : (x[1], x[0]))
et = 0
cnt =0
for s, e in meeting:
    if s>=et:
        et=e
        cnt+=1
    
print(meeting)