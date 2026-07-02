'''
    t초 x회복 연속 붕대  성공 시 y 체력 회복 최대체력까지만
    현재 시간 변수
    attack for문 돌리면서 현재시간, 시간 비교해서 회복 량 비교 최대체력까지만
'''
def solution(bandage, mx_health, attacks):
    time = 0
    health = mx_health
    t, x, y = bandage
    
    for a_time, dmg in attacks:
        연속 = (a_time - time -1) // t
        나머지 = a_time - time - 1
        health += 연속 * y + 나머지 * x
        if health > mx_health:
            health = mx_health
        
        health -= dmg
        
        if health <= 0: return -1
        time = a_time

    return health


def solution(bandage, mx_health, attacks):
    t, x, y = bandage
    health = mx_health
    current_time = 0
    
    for attack_time, dmg in attacks:
        # 1. 공격 사이의 시간 동안 붕대 감기 진행
        gap = attack_time - current_time - 1
        
        # gap 동안의 일반 회복
        health += gap * x
        # gap 동안 추가 회복(y)이 몇 번 발생하는지 계산
        health += (gap // t) * y
        
        # 최대 체력을 넘지 않도록 제한
        if health > mx_health:
            health = mx_health
            
        # 2. 몬스터 공격 적용
        health -= dmg
        
        # 체력이 0 이하가 되면 사망
        if health <= 0:
            return -1
        
        # 시간 갱신
        current_time = attack_time
        
    return health