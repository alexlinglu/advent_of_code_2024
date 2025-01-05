import re

def move(map, direction, position):
    if direction == (-1, 0): #move up
        for i in reversed(range(position[0])):
            if(map[i][position[1]] == '#'):
                #print(position)
                return move(map, (0, 1), (i + 1, position[1]))
            map[i] = map[i][0:position[1]] + "X" + map[i][position[1] + 1:len(map[i])]
    elif direction == (0, 1): #move right
        for i in range(len(map[0]) - position[1]):
            if(map[position[0]][i + position[1]] == '#'):
                return move(map, (1, 0), (position[0], i + position[1] - 1))
            map[position[0]] = map[position[0]][0:i+position[1]] + "X" + map[position[0]][i+position[1]+1:len(map[position[0]])]
    elif direction == (1, 0): #move down
        for i in range(len(map) - position[0]):
            if(map[i + position[0]][position[1]] == '#'):
                return move(map, (0, -1), (i + position[0] - 1, position[1]))
            map[i + position[0]] = map[i + position[0]][0:position[1]] + "X" + map[i + position[0]][position[1]+1:len(map[i + position[0]])]
    elif direction == (0, -1): #move left
        for i in reversed(range(position[1])):
            if(map[position[0]][i] == '#'):
                return move(map, (-1, 0), (position[0], i + 1))
            map[position[0]] = map[position[0]][0:i] + "X" + map[position[0]][i+1:len(map[position[0]])]
    return map

with open("input.txt", "r") as file:
   input_data = file.readlines()

areaMap = []
total = 0
for line in input_data:
    areaMap.append(line[0:130])

areaMap = move(areaMap, (-1, 0), (40, 46))
for row in areaMap:
    print(row)
    total += len(re.findall("X", row))
print(total)