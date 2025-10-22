def solution(name):
    # 각 위치에서 알파벳을 바꾸는 데 필요한 최소 조작 횟수 계산
    change = [min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name]
    answer = sum(change)
    print(answer)
    move = len(name) - 1  # 커서를 오른쪽으로만 이동할 때 가장 멀리 이동한 값

    for i in range(len(name)):
        next_i = i + 1
        # 연속된 'A'를 건너뛰기 위해 다음 문자가 A가 아닌 곳을 찾는다.
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        # 오른쪽으로 갔다가 왼쪽으로 돌아오는 경우의 최소 이동을 고려
        move = min(move, 2 * i + len(name) - next_i, i + 2 * (len(name) - next_i))
        print(move)
    print(move)
    return answer + move

solution("JAAZ")