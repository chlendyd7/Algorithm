class day:
    def __init__(self, month, day):
        self.month = month
        self.day = day

def solution():
    day_dict = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31,
    }

    lst = list(map(int, input().split()))
    day1 = day(lst[0], lst[1])
    day2 = day(lst[2], lst[3])
    cnt = 0
    if day1.month != day2.month:
        cnt += day_dict[day1.month] - day1.day + 1
        while day1.month != day2.month:
            day1.month += 1
            if day1.month != day2.month:
                cnt += day_dict[day1.month]
            else:
                cnt += day2.day
    else:
        cnt += day2.day - day1.day + 1
    
    
    return cnt

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
