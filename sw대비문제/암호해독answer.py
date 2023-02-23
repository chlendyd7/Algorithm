import sys

def calc(key, n, words):
    for i in range(26):
        temp = ""
        for k in key:
            temp += chr(((ord(k)-97 + i)%26)+97)
        for k in range(n):
            if words[k] in temp:
                return temp





key= sys.stdin.readline()# 줄바꿈 문자 제거
n=int(sys.stdin.readline())
words = []
for i in range(n):
    word = input()
    words.append(word)

print(calc(key , n, words))