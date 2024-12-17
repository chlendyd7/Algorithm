from datetime import date

def add_months_to_date(start_date, months):
    new_year = start_date.year + (start_date.month + months - 1) // 12
    new_month = (start_date.month + months - 1) % 12 + 1
    return date(new_year, new_month, start_date.day)

def solution(today, terms, privacies):
    answer = []

    today_year, today_month, today_day = map(int, today.split('.'))
    today_date = date(today_year, today_month, today_day)

    terms_dict = dict()
    for term in terms:
        key, value = term.split()
        terms_dict[key] = int(value)
    
    for idx, privacy in enumerate(privacies):
        date_str, temrs_type = privacy.split()
        year, month, day = map(int, date_str.split('.'))
        collected_date = date(year, month, day)

        expiration_date = add_months_to_date(collected_date, terms_dict[temrs_type])

        if expiration_date <= today_date:
            answer.append(idx + 1)
    
    return answer