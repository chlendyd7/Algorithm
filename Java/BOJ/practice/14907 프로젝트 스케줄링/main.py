import sys

tasks = {}
for line in sys.stdin:
    # line.strip()을 안 하면 줄바꿈 문자가 포함될 수 있으니 주의!
    parts = line.split()
    if not parts:
        break
    
    name = parts[0]
    time = int(parts[1])
    pre = parts[2] if len(parts) == 3 else ""
    tasks[name] = (time, pre)
