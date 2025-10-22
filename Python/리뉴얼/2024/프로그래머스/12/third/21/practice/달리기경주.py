def solution(players, callings):
    players_dict = { player: idx for idx, player in enumerate(players) }
    
    for call in callings:
        idx = players_dict[call]
        players[idx], players[idx-1] = players[idx-1], players[idx]
        players_dict[players[idx]] = idx
        players_dict[players[idx-1]] = idx - 1
    return players