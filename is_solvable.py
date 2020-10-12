def isPuzzleConform(solved_state, puzzle):
    try:
        for i in puzzle:
            if i not in solved_state:
                return 0
    except ValueError:
        return 0
    return 1

def getInvCount(puzzle, solved_state, size):
    inv_count = 0
    for i in range(size * size - 1):
        for j in range(i + 1, size * size):            
            if puzzle[i] and puzzle[j] and solved_state.index(puzzle[i]) > solved_state.index(puzzle[j]):
                inv_count += 1
    return inv_count
    
def isSolvable(puzzle, size, solved_state):
    if isPuzzleConform(solved_state, puzzle) != 0:
        return getInvCount(puzzle, solved_state, size) % 2 == 0
    else:
        return 0