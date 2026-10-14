def solve_magic(requirements, spells):
    stack = []
    total_uses = 0

    for m_type, m_mana in spells:
        curr_type = m_type
        curr_mana = m_mana

        while stack and stack[-1][0] == curr_type:
            prev_type, prev_mana = stack.pop()
            curr_mana += prev_mana
        
        if curr_mana >= requirements[curr_type]:
            total_uses += 1
        else:
            stack.append([curr_type, curr_mana])
    