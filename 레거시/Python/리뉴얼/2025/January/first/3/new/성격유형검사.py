def solution(survey, choices):
    # 1. 성격 유형 점수를 저장할 딕셔너리 초기화
    scores = {char: 0 for char in "RTCFJMAN"}
    
    # 2. 설문조사와 선택지 처리
    for q, choice in zip(survey, choices):
        type1, type2 = q  # 예: 'RT' -> type1='R', type2='T'
        score = abs(choice - 4)  # 선택지에서 중립(4)와의 거리
        if choice < 4:
            scores[type1] += score  # 비동의: type1에 점수 추가
        elif choice > 4:
            scores[type2] += score  # 동의: type2에 점수 추가

    # 3. 각 지표별로 점수를 비교해 성격 유형 결정
    result = ""
    result += "R" if scores["R"] >= scores["T"] else "T"
    result += "C" if scores["C"] >= scores["F"] else "F"
    result += "J" if scores["J"] >= scores["M"] else "M"
    result += "A" if scores["A"] >= scores["N"] else "N"

    return result
