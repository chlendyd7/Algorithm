def solution(players, callings):
    player_idx = { player : idx for idx, player in enumerate(players) }
    
    for call in callings:
        idx = player_idx[call] # 3
        players[idx - 1], players[idx] = players[idx], players[idx - 1]

        
        player_idx[players[idx]] = idx
        player_idx[players[idx -1]] = idx - 1

    return players
