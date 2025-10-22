# 균형잡힌 세상
import sys; input= sys.stdin.readline

while input != '.':
    string = input().rstrip()
    if string == '.': break
    for s in string:
        if s not in '()[]':
            string = string.replace(s,'')
    while '[]' in string or '()' in string:
        string = string.replace('()','')
        string = string.replace('[]','')
    print('no') if string else print('yes')
    