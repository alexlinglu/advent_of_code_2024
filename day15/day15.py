import re

def move(instruction, position):
    directions = {
        "<": (0, -1),
        "v": (1, 0),
        ">": (0, 1),
        "^": (-1, 0)
    }
    direction = directions[instruction]

    if area_map[position[0] + direction[0]][position[1] + direction[1]] == "#":
        return False
    elif area_map[position[0] + direction[0]][position[1] + direction[1]] == "." or move(instruction, (position[0] + direction[0], position[1] + direction[1])):
        temp = area_map[position[0]][position[1]]
        area_map[position[0]] = area_map[position[0]][0:position[1]] + area_map[position[0] + direction[0]][position[1] + direction[1]] + area_map[position[0]][position[1] + 1:]
        area_map[position[0] + direction[0]] = area_map[position[0] + direction[0]][0:position[1] + direction[1]] + temp + area_map[position[0] + direction[0]][position[1] + direction[1] + 1:]
        return (position[0] + direction[0], position[1] + direction[1])
    return False

with open("input.txt", "r") as file:
    input_data = file.read()

map_end = re.search("\n\n", input_data).start()
area_map = input_data[0:map_end].split("\n")
instructions = input_data[map_end + 2:].replace("\n", "")
for i in range(len(area_map)):
    if re.search("@", area_map[i]):
        robot_position = (i, re.search("@", area_map[i]).start())
        break
for instruction in instructions:
    new_position = move(instruction, robot_position)
    if new_position:
        robot_position = new_position

total_coords = 0
for y in range(len(area_map)):
    box_x = [m.start() for m in re.finditer("O", area_map[y])]
    for x in box_x:
        total_coords += y * 100 + x
print(total_coords)