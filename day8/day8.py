import re

with open("input.txt", "r") as file:
    input_data = file.read()

antinode_map = ""
for node in input_data:
    if node == "\n":
        antinode_map += "\n"
    else:
        antinode_map += "."

r = re.compile(r"\w")
antennas = [(m.group(0), m.start()) for m in r.finditer(input_data)] #tuples of (character, position)
for i in range(len(antennas)):
    for j in range(i + 1, len(antennas)):
        if antennas[i][0] == antennas[j][0]:
            first_antinode = antennas[i][1] - (antennas[j][1] - antennas[i][1]) #position based on index of string
            second_antinode = antennas[j][1] + (antennas[j][1] - antennas[i][1])
            antenna_lines_passed = 0
            for k in range(antennas[i][1], antennas[j][1]):
                if input_data[k] == "\n":
                    antenna_lines_passed += 1

            if first_antinode >= 0 and not input_data[first_antinode] == "\n":
                first_lines_passed = 0
                for k in range(first_antinode, antennas[i][1]):
                    if input_data[k] == "\n":
                        first_lines_passed += 1
                if first_lines_passed == antenna_lines_passed:
                    antinode_map = antinode_map[0:first_antinode] + "#" + antinode_map[first_antinode+1:]
                    
            if second_antinode < len(input_data) and not input_data[second_antinode] == "\n":
                second_lines_passed = 0
                for k in range(antennas[j][1], second_antinode):
                    if input_data[k] == "\n":
                        second_lines_passed += 1
                if second_lines_passed == antenna_lines_passed:
                    antinode_map = antinode_map[0:second_antinode] + "#" + antinode_map[second_antinode+1:]
print(antinode_map)
print(len(re.findall(r"#", antinode_map)))