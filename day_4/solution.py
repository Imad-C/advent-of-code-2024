def _get_neighbour_coord(coord, neighbour_direction):
    return [
        coord[0] + neighbour_direction[0], + coord[1] + neighbour_direction[1]]


def _check_bounds(val, l_bound, h_bound):
    if val < l_bound or val >= h_bound:
        return False
    return True


def find_term(data, string, coord, direction):
    # base case, if no more string, then all letters have been found
    if len(string) == 0:
        return True

    x, y = coord
    if not (_check_bounds(x, 0, len(data[0])) and _check_bounds(y, 0, len(data))):
        return False

    # if letter matches first letter of string, move on to neighbour
    if data[x][y] == string[0]:
        neighbour_coord = _get_neighbour_coord([x, y], direction)
        return find_term(
            data=data, string=string[1:], coord=neighbour_coord, direction=direction)

    return False


## Task 1
# list of lists, i.e. 2D array
data = [list(l.split()[0]) for l in open('day_4/input.txt')]

directions = [
    [-1, -1], [0, -1], [1, -1],
    [-1, 0], [1, 0],
    [-1, 1], [0, 1], [1, 1]]

xmas_counter = 0
for x in range(0, len(data[0])):
    for y in range(len(data)):
        for direction in directions:
            if find_term(data, 'XMAS', [x, y], direction):
                xmas_counter += 1

print(f'Task 1: {xmas_counter}') # 2401


## Task 2
# only care about diagonals
directions = [
    [-1, -1], [1, -1],
    [-1, 1], [1, 1]]

xmas_counter = 0
for x in range(0, len(data[0])):
    for y in range(len(data)):
        if not (
            _check_bounds(x, 0, len(data[0]) - 2) and\
            _check_bounds(y, 0, len(data) - 2)
                ):
            continue 

        small_data = [data[x][y:y+3], data[x+1][y:y+3], data[x+2][y:y+3]]

        mas_counter = 0
        for x_small in range(0, len(small_data[0])):
            for y_small in range(0, len(small_data)):
                for direction in directions:
                    if find_term(small_data, 'MAS', [x_small, y_small], direction):
                        mas_counter += 1
        if mas_counter >= 2:
            xmas_counter += 1

print(f'Task 2: {xmas_counter}') # 1822