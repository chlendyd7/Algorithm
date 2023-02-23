# 입력된 값을 변환하기
# 아스키 코드로 들어옴
# 일단 더해야함
# if문돌리면서 커지면 - 몇 해야함
# 아스키코드 65 ~ 122
# 대문자 65 ~ 90
#소문자 97 ~ 122
pw = input()
pw = list(pw)
for i in range(len(pw)):
    if pw[i].isupper():
        if pw[i] > 90:
            tmp = ord(pw[i])
            tmp = chr(tmp - 17)
        else:    
            pw[i] = tmp


print(pw)
