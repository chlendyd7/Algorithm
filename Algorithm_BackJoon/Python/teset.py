words = input().upper()
words2 = list(set(words))#for문을 돌리기 위해 알파벳의 갯수를 맞추어줌
cnt_list= []
for x in words2:
    cnt = words.count(x)#wods2에 있는 알파벳이 words에 몇개가 들어있는가를 맞춰줌
    cnt_list.append(cnt)#각 알파벳의 갯수를 cnt_list에 append
if cnt_list.count(max(cnt_list))>1:
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list))
    print(words2[max_index])
    print(cnt_list)#cnt_list는 랜덤으로 들어가게된다.
    print(max_index)