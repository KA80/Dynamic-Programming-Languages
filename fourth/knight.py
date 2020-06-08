def list_of_turns(cell, i=None):
    possible_pos = []
    x, y = coord_translation_to_int(cell)
    possible_pos.append([x + 2, y + 1])
    possible_pos.append([x + 2, y - 1])
    possible_pos.append([x - 2, y + 1])
    possible_pos.append([x - 2, y - 1])
    possible_pos.append([x + 1, y + 2])
    possible_pos.append([x + 1, y - 2])
    possible_pos.append([x - 1, y + 2])
    possible_pos.append([x - 1, y - 2])
    i = 0
    while i != len(possible_pos):
        checker = check_in_board(possible_pos[i])
        if not checker:
            possible_pos.pop(i)
        else:
            possible_pos[i] = coord_translation_to_str(possible_pos[i])
            i += 1
    return sorted(possible_pos)


def coord_translation_to_str(cell):
    horizontal = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
    return horizontal[cell[0]] + str(cell[1])


def coord_translation_to_int(cell):
    horizontal = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
    return horizontal[cell[0]], int(cell[1])


def check_in_board(possible_pos):
    if 1 <= possible_pos[0] <= 8 and 1 <= possible_pos[1] <= 8:
        return True
    else:
        return False


pos = input()
print(*list_of_turns(pos))
