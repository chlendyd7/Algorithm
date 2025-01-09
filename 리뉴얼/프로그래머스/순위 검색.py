from collections import defaultdict
from bisect import bisect_left
from itertools import combinations

def solution(info, query):
    answer = []
    info_map = defaultdict(list)

    # 지원자 정보 해싱
    for person in info:
        details = person.split()
        score = int(details.pop())  # 점수 분리
        for r in range(5):  # 조합 수: 0 ~ 4
            # 다양한 조합과 매칭되기 위해
            for comb in combinations(range(4), r): 
                key = details[:]  # 세부정보 복사
                for idx in comb:
                    key[idx] = "-"  # 조합에 포함된 요소를 '-'로 대체
                info_map[" ".join(key)].append(score)

    # 점수 리스트 정렬
    for key in info_map:
        info_map[key].sort()

    # 쿼리 처리
    for q in query:
        # 'and' 제거 및 점수 분리
        conditions = q.replace(" and", "").split()
        target_score = int(conditions.pop())  # 타겟 점수
        target_key = " ".join(conditions)  # 검색 키 생성

        # 해당 조건에 맞는 점수 리스트
        scores = info_map[target_key]

        # 조건에 맞는 지원자가 없는 경우
        if not scores:
            answer.append(0)
            continue

        # lower bound 탐색
        start_idx = bisect_left(scores, target_score)
        answer.append(len(scores) - start_idx)  # 조건을 만족하는 지원자 수

    return answer
