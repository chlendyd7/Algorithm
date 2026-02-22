n=int(input())
title = "666"
title_cnt = 0
tt_cnt = 0
while True:
    if title in str(title_cnt):
        tt_cnt +=1
    if tt_cnt == n:
        print(title_cnt)
        break
    title_cnt +=1
