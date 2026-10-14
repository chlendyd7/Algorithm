'''
파일명은 우선 HEAD 부분을 기준으로 사전 순으로 정렬한다. 이때, 문자열 비교 시 대소문자 구분을 하지 않는다. MUZI와 muzi, MuZi는 정렬 시에 같은 순서로 취급된다

파일명의 HEAD 부분이 대소문자 차이 외에는 같을 경우, NUMBER의 숫자 순으로 정렬한다. 9 < 10 < 0011 < 012 < 13 < 014 순으로 정렬된다. 숫자 앞의 0은 무시되며, 012와 12는 정렬 시에 같은 같은 값으로 처리된다.

두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지한다. MUZI01.zip과 muzi1.png가 입력으로 들어오면, 정렬 후에도 입력 시 주어진 두 파일의 순서가 바뀌어서는 안 된다.

for문을 한번 돌려서 head, number, index 로 분리
lambda를 사용해서 lambda x: (x[0], int(x[1])) 이렇게 하면 되려나?

index를 관리해서 원본을 보존 하여 list에 넣어보자

2번 케이스의 경우 어떻게 처리해야하는가
'''
# isdigit
def solution(files):
    first_lst = []
    for file in files:
        start = -1
        end = -1
        
        for i in range(len(file)):
            if file[i].isdigit():
                if start == -1:
                    start = i
            elif start != -1:
                end = i
                break
        if end == -1:
            end = len(file)

        first_lst.append((file[:start], file[start:end], file))

        first_lst.sort(key=lambda x:(x[0].lower(), int(x[1])))
    
    return [item[2] for item in first_lst]
