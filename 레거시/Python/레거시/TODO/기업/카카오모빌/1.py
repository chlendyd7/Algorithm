from datetime import date

def add_months_to_date(start_date, months):
    # 시작 날짜에 월을 더하여 새로운 날짜를 계산하는 함수
    new_year = start_date.year + (start_date.month + months - 1) // 12
    new_month = (start_date.month + months - 1) % 12 + 1
    return date(new_year, new_month, start_date.day)

def solution(today: str, terms: list, privacies: list) -> list:
    answer = []
    
    # 오늘 날짜 파싱
    today_year, today_month, today_day = map(int, today.split('.'))
    today_date = date(today_year, today_month, today_day)
    
    # 약관의 유효기간을 저장할 딕셔너리
    terms_dict = {}
    for term in terms:
        key, value = term.split()
        terms_dict[key] = int(value)
    
    # 개인정보의 유효기간 체크
    for idx, privacy in enumerate(privacies):
        date_str, term_type = privacy.split()
        year, month, day = map(int, date_str.split('.'))
        collected_date = date(year, month, day)
        
        # 유효기간 계산
        expiration_date = add_months_to_date(collected_date, terms_dict[term_type])
        
        # 오늘 날짜와 비교하여 유효기간이 지났는지 확인
        if expiration_date <= today_date:
            answer.append(idx + 1)  # 인덱스를 1부터 시작하도록 하기 위해 +1
    
    return answer

