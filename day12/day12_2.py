surveyed = set()
to_survey = [(0, 0)]
partial_sides = set()

def check_side(node, direction, bounded):
    partial_sides.add(((node, direction), input_data[node[0]][node[1]]))
    counter_clockwise = (direction[1], direction[0]) #not always counter-clockwise, 90 degree turn
    clockwise = (-direction[1], -direction[0])
    counter_clockwise_in_bounds = node[0] + counter_clockwise[0] >= 0 and node[0] + counter_clockwise[0] < len(input_data) and node[1] + counter_clockwise[1] >= 0 and node[1] + counter_clockwise[1] < len(input_data)
    clockwise_in_bounds = node[0] + clockwise[0] >= 0 and node[0] + clockwise[0] < len(input_data) and node[1] + clockwise[1] >= 0 and node[1] + clockwise[1] < len(input_data)

    while counter_clockwise_in_bounds and input_data[node[0] + counter_clockwise[0]][node[1] + counter_clockwise[1]] == input_data[node[0]][node[1]] and (bounded or input_data[node[0] + counter_clockwise[0] + direction[0]][node[1] + counter_clockwise[1] + direction[1]] != input_data[node[0]][node[1]]):
        if (((node[0] + counter_clockwise[0], node[1] + counter_clockwise[1]), direction), input_data[node[0]][node[1]]) in partial_sides:
            return 0
        counter_clockwise = (counter_clockwise[0] + direction[1], counter_clockwise[1] + direction[0])
        counter_clockwise_in_bounds = node[0] + counter_clockwise[0] >= 0 and node[0] + counter_clockwise[0] < len(input_data) and node[1] + counter_clockwise[1] >= 0 and node[1] + counter_clockwise[1] < len(input_data)
    while clockwise_in_bounds and input_data[node[0] + clockwise[0]][node[1] + clockwise[1]] == input_data[node[0]][node[1]] and (bounded or input_data[node[0] + clockwise[0] + direction[0]][node[1] + clockwise[1] + direction[1]] != input_data[node[0]][node[1]]):
        if (((node[0] + clockwise[0], node[1] + clockwise[1]), direction), input_data[node[0]][node[1]]) in partial_sides:
            return 0
        clockwise = (clockwise[0] - direction[1], clockwise[1] - direction[0])
        clockwise_in_bounds = node[0] + clockwise[0] >= 0 and node[0] + clockwise[0] < len(input_data) and node[1] + clockwise[1] >= 0 and node[1] + clockwise[1] < len(input_data)
    return 1

def survey(node, map):
    surveyed.add(node)
    area = 1
    sides = 0

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    if node[0] == 0:
        directions.remove((-1, 0))
        sides += check_side(node, (-1, 0), True)
    elif node[0] == len(map) - 1:
        directions.remove((1, 0))
        sides += check_side(node, (1, 0), True)
    if node[1] == 0:
        directions.remove((0, -1))
        sides += check_side(node, (0, -1), True)
    elif node[1] == len(map[0]) - 1:
        directions.remove((0, 1))
        sides += check_side(node, (0, 1), True)

    for direction in directions:
        if (node[0] + direction[0], node[1] + direction[1]) not in surveyed:
            if map[node[0] + direction[0]][node[1] + direction[1]] == map[node[0]][node[1]]:
                a_increase, p_increase = survey((node[0] + direction[0], node[1] + direction[1]), map)
                area += a_increase
                sides += p_increase
                if (node[0] + direction[0], node[1] + direction[1]) in to_survey:
                    to_survey.remove((node[0] + direction[0], node[1] + direction[1]))
            else:
                sides += check_side(node, direction, False)
                if (node[0] + direction[0], node[1] + direction[1]) not in to_survey:
                    to_survey.append((node[0] + direction[0], node[1] + direction[1]))
        elif map[node[0] + direction[0]][node[1] + direction[1]] != map[node[0]][node[1]]:
            sides += check_side(node, direction, False)
    return (area, sides)

with open("input.txt", "r") as file:
    input_data = file.readlines()
for i in range(len(input_data)):    
    input_data[i] = input_data[i][0:len(input_data)]

total = 0
while len(to_survey) != 0:
    area, sides = survey(to_survey[0], input_data)
    total += area * sides   
    to_survey.pop(0)
print(total)