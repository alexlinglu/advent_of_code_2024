surveyed = set()
to_survey = [(0, 0)]

def survey(node, map):
    surveyed.add(node)
    area = 1
    perimeter = 0

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    if node[0] == 0:
        directions.remove((-1, 0))
        perimeter += 1
    elif node[0] == len(map) - 1:
        directions.remove((1, 0))
        perimeter += 1
    if node[1] == 0:
        directions.remove((0, -1))
        perimeter += 1
    elif node[1] == len(map[0]) - 1:
        directions.remove((0, 1))
        perimeter += 1

    for direction in directions:
        if (node[0] + direction[0], node[1] + direction[1]) not in surveyed:
            if map[node[0] + direction[0]][node[1] + direction[1]] == map[node[0]][node[1]]:
                a_increase, p_increase = survey((node[0] + direction[0], node[1] + direction[1]), map)
                area += a_increase
                perimeter += p_increase
                if (node[0] + direction[0], node[1] + direction[1]) in to_survey:
                    to_survey.remove((node[0] + direction[0], node[1] + direction[1]))
            else:
                perimeter += 1
                if (node[0] + direction[0], node[1] + direction[1]) not in to_survey:
                    to_survey.append((node[0] + direction[0], node[1] + direction[1]))
        elif map[node[0] + direction[0]][node[1] + direction[1]] != map[node[0]][node[1]]:
            perimeter += 1
    return (area, perimeter)

with open("input.txt", "r") as file:
    input_data = file.readlines()
for i in range(len(input_data)):
    input_data[i] = input_data[i][0:len(input_data)]

total = 0
while len(to_survey) != 0:
    area, perimeter = survey(to_survey[0], input_data)
    total += area * perimeter
    to_survey.pop(0)
print(total)
