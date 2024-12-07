# list of lists, i.e. 2D array
data = [list(l.split()[0]) for l in open('day_4/input.txt')]
grid_width = len(data[0])
grid_length = len(data)


def _get_neighbour_coord(coord, neighbour_direction):
    return [
        coord[0] + neighbour_direction[0], + coord[1] + neighbour_direction[1]]


def _check_bounds(val, l_bound, h_bound):
    if val < l_bound or val >= h_bound:
        return False
    return True


def find_term(string, coord, direction):
    # base case, if no more string, then all letters have been found
    if len(string) == 0:
        return True

    x, y = coord
    if not (_check_bounds(x, 0, grid_width) and _check_bounds(y, 0, grid_length)):
        return False

    # if letter matches first letter of string, move on to neighbour
    if data[x][y] == string[0]:
        neighbour_coord = _get_neighbour_coord([x, y], direction)
        return find_term(
            string=string[1:], coord=neighbour_coord, direction=direction)

    return False


## Task 1
directions = [
    [-1, -1], [0, -1], [1, -1],
    [-1, 0], [1, 0],
    [-1, 1], [0, 1], [1, 1]]

xmas_counter = 0
for x in range(0, len(data[0])):
    for y in range(len(data)):
        for direction in directions:
            if find_term('XMAS', [x, y], direction):
                xmas_counter += 1

print(f'Task 1: {xmas_counter}') # 2401


## Task 2
# only care about diagonals
# directions = [
#     [-1, -1], [1, -1],
#     [-1, 1], [1, 1]]

# xmas_counter = 0
# for x in range(0, len(data[0])):
#     for y in range(len(data)):
#         if not _check_bounds([x, y], )
#         for direction in directions:
#             if find_term('MAS', [x, y], direction):
#                 xmas_counter += 1
#             corner_points = 