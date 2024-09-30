# https://www.acmicpc.net/problem/20437
'''
가장 짧은 연속 문자열
문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
'''
from collections import defaultdict


T = int(input())
for _ in range(T):
    long_str = -1
    min_str = float('inf')
    string = input()
    k = int(input())
    dic = defaultdict(list)

    for i in range(len(string)):
        if string.count(string[i]) >= k:
            dic[string[i]].append(i)
    
    if not dic:
        print(-1)
    else:
        small = float('inf')
        big = 0

        for alpha in dict:
            for i in range(len(dict[alpha] - k + 1)):
                length = dic[alpha][i+k-1] - dic[alpha][i]+1
        alp = string[i]
        cnt = 0
        for j in range(i+1, len(string)):
            if alp == string[j]:
                cnt += 1
            if cnt == k:
                long_str = max(long_str, j-i)
                min_str = min(min_str, j-i)
    if long_str == -1:
        print(-1)
    else:
        print(min_str, long_str)

