T = int(input())
for tc in range(1, T+1):
    n = int(input())
    current_speed = 0
    result = 0
    for _ in range(n):
        now_input = input()
        if len(now_input) == 3:
            cmd, speed = map(int, now_input.split())
            if cmd == 1:
                current_speed += speed
            elif cmd == 2:
                current_speed -= speed
                if current_speed < 0:
                    current_speed = 0
        result += current_speed
        
    print(f'#{tc} {result}')
