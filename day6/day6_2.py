def checkLoop(map, direction, position, lastCyclePositions):
    if direction == (-1, 0): #move up
        if position in lastCyclePositions:
            return True
        for i in reversed(range(position[0])):
            if(map[i][position[1]] == '#'):
                lastCyclePositions.append(position)
                return checkLoop(map, (0, 1), (i + 1, position[1]), lastCyclePositions)
            map[i] = map[i][0:position[1]] + "X" + map[i][position[1] + 1:len(map[i])]
    elif direction == (0, 1): #move right
        for i in range(len(map[0]) - position[1]):
            if(map[position[0]][i + position[1]] == '#'):
                return checkLoop(map, (1, 0), (position[0], i + position[1] - 1), lastCyclePositions)
            map[position[0]] = map[position[0]][0:i+position[1]] + "X" + map[position[0]][i+position[1]+1:len(map[position[0]])]
    elif direction == (1, 0): #move down
        for i in range(len(map) - position[0]):
            if(map[i + position[0]][position[1]] == '#'):
                return checkLoop(map, (0, -1), (i + position[0] - 1, position[1]), lastCyclePositions)
            map[i + position[0]] = map[i + position[0]][0:position[1]] + "X" + map[i + position[0]][position[1]+1:len(map[i + position[0]])]
    elif direction == (0, -1): #move left
        for i in reversed(range(position[1])):
            if(map[position[0]][i] == '#'):
                return checkLoop(map, (-1, 0), (position[0], i + 1), lastCyclePositions)
            map[position[0]] = map[position[0]][0:i] + "X" + map[position[0]][i+1:len(map[position[0]])]
    return False

with open("input.txt", "r") as file:
   input_data = file.readlines()

areaMap = []
total = 0
for line in input_data:
    areaMap.append(line[0:130])

for i in range(len(areaMap)):
    for j in range(len(areaMap[0])):
        if areaMap[i][j] == '.' or i == 40 and j == 46:
            mapToCheck = areaMap.copy()
            mapToCheck[i] = mapToCheck[i][0:j] + "#" + mapToCheck[i][j+1:len(areaMap[0])]
            positions = [(-1, -1)]
            if checkLoop(mapToCheck, (-1, 0), (40, 46), positions):
                total += 1
print(total)