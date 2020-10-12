from heapq import heappush, heappop
from itertools import count

def reconstructPath(node, parent, closed_list):
    path = [node]
    while parent is not None:
        path.append(parent)
        parent = closed_list[parent]
    return path[::-1]

def copy_swap(data, current, goal):
    cpy = list(data)

    tmp = cpy[current]
    cpy[current] = cpy[goal]
    cpy[goal] = tmp
    
    return tuple(cpy) 

def possibleChildren(data, size):
    children = []
    empty_tile_index = data.index(0)

    if empty_tile_index % size > 0:
        left = copy_swap(data, empty_tile_index, empty_tile_index - 1)
        children.append(left)

    if empty_tile_index % size + 1 < size:
        right = copy_swap(data, empty_tile_index, empty_tile_index + 1)
        children.append(right)

    if empty_tile_index - size >= 0:
        up = copy_swap(data, empty_tile_index, empty_tile_index - size)
        children.append(up)

    if empty_tile_index + size < len(data):
        down = copy_swap(data, empty_tile_index, empty_tile_index + size)
        children.append(down)

    return children

def aStarOptimized(puzzle, solved_state, size, heuristic):
    c = count()
    # (fscore, iterator, state, g_state, parent) #
    queue = [(0, next(c), puzzle, 0, None)]
    open_set = {}
    closed_list = {}
    while queue:
        _, _, node, node_g, parent = heappop(queue)

        if node == solved_state:
            path = reconstructPath(node, parent, closed_list)
            return (True, path, {'space':len(open_set), 'time':len(closed_list)})
        
        if node in closed_list:
            continue
        
        closed_list[node] = parent
        tmp_g = node_g + 1

        children = possibleChildren(node, size)

        for child in children:

            if child in closed_list:
                continue
            
            if child in open_set:
                child_g, child_h = open_set[child]
                
                if child_g < tmp_g:
                    continue
            else:
                child_h = heuristic(child, solved_state, size)
            open_set[child] = tmp_g, child_h
            heappush(queue, (child_h + tmp_g, next(c), child, tmp_g, node))
    return (False, None, {'space':len(open_set), 'time':len(closed_list)})