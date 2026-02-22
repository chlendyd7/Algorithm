def solution(config):
    # config 리스트에서 key-value 쌍을 딕셔너리로 생성
    k = dict()
    for i in range(0, len(config), 2):
        if i + 1 < len(config):
            k[config[i]] = config[i + 1]
    
    # 결과 리스트 초기화
    result = []
    
    for i in range(0, len(config), 2):
        key = config[i]
        value = config[i + 1]
        
        # value에서 {key} 형태로 되어 있는 부분을 실제 값으로 치환
        for inner_key in k.keys():
            if f"{{{inner_key}}}" in value:
                value = value.replace(f"{{{inner_key}}}", k[inner_key])
        
        # 결과 리스트에 키와 값을 순서대로 추가
        result.append(key)
        result.append(value)
    
    return result

# 테스트 입력
t = ["test", "test!!", "test2", "{test} is {test}!!"]
print(solution(t))
