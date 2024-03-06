n = int(input())
meeting = []
for i in range(n):
    s, e=map(int, input().split())
    meeting.append((s,e))

meeting.sort(reverse=True)
print(meeting)
    