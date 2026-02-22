def solution(players, callings):
    player_idx = {player: idx for idx, player in enumerate(players)}
    
    for call in callings:
        idx = player_idx[call]
        players[idx], players[idx - 1] = players[idx - 1], players[idx]  # 스와핑
        
        # 스왑 후 인덱스 갱신
        player_idx[players[idx]] = idx
        player_idx[players[idx - 1]] = idx - 1

    return players
