def manhatthanDistance(current_state, solved_state, size):
    res = 0
    for i in range(size * size):
        if current_state[i] != 0 and current_state[i] != solved_state[i]:
            index = solved_state.index(current_state[i])
            y = (i // size) - (index // size)
            x = (i % size) - (index % size)
            res += abs(y) + abs(x)
    return res

def euclideanDistance(current_state, solved_state, size):
    res = 0
    for i in range(size * size):
        if current_state[i] != 0 and current_state[i] != solved_state[i]:
            index = solved_state.index(current_state[i])
            y = (i // size) - (index // size)
            x = (i % size) - (index % size)
            res += pow(y, 2) + pow(x, 2)
    return res

def tilesOutOfPlace(current_state, solved_state, size):
    res = 0
    for i in range(size * size):
        if current_state[i] != 0 and current_state[i] != solved_state[i]:
            res += 1
    return res

def heuristics(choice):
    functions = [manhatthanDistance, euclideanDistance, tilesOutOfPlace]
    return functions[choice]
