import re
import math

with open("input.txt", "r") as file:
    input_data = file.read()

line_size = re.search(r"\n", input_data).start() + 1
r = re.compile(r"0")
possible_routes = [((math.floor(m.start() / line_size), m.start() % line_size), (0, 0)) for m in r.finditer(input_data)] #stores nodes with position and previous direction
input_data_map = []
for i in range(math.floor(len(input_data) / line_size)):
    input_data_map.append(input_data[i * line_size:(i + 1) * line_size])

total = 0
while len(possible_routes) > 0:
    position = possible_routes[0][0]
    prev_direction = possible_routes[0][1]
    if input_data_map[position[0]][position[1]] == "9":
        total += 1
    else:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        if position[0] == 0:
            directions.remove((-1, 0))
        elif position[0] == len(input_data_map) - 1:
            directions.remove((1, 0))
        if position[1] == 0:
            directions.remove((0, -1))
        elif position[1] == len(input_data_map[0]) - 1:
            directions.remove((0, 1))
        if prev_direction in directions:
            directions.remove(prev_direction)

        for direction in directions:
            if input_data_map[position[0] + direction[0]][position[1] + direction[1]] != "\n" and int(input_data_map[position[0] + direction[0]][position[1] + direction[1]]) == int(input_data_map[position[0]][position[1]]) + 1:
                possible_routes.append(((position[0] + direction[0], position[1] + direction[1]), (direction[0] * -1, direction[1] * -1)))
    possible_routes.pop(0)
print(total)