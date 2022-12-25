# 해쉬
a = int(input())
p=dict()
# 딕셔너리 타입은 immutable한 키(key)와 mutable한 값(value)으로 맵핑되어 있는 순서가 없는 집합입니다
# 순서가 없어 key 값으로 접근 해야함
for i in range(a):
    word = input()
    p[word]=1 # ?: 단어를 읽고 key 값이 됨

for i in range(a-1):
    word = input()
    p[word]=0
#이 for문에서 dict의 단어를 0으로 바꿈

for key, val in p.items():
# key와 value를 한꺼번에 for문을 반복하려면 items() 를 사용합니다.
    if val == 1:
        print(key)
        break
1