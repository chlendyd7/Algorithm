a = input().upper()
set_a = list(set(a))
cnt_list =[]
for x in set_a:
    cnt = a.count(x)
    cnt_list.append(cnt)

if cnt_list(max(cnt_list))>1:
    print("?")