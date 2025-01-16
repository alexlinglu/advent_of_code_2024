import re

with open("input.txt", "r") as file:
    input_data = file.readlines()

width = 101
height = 103
max_times = 101 * 103
robots = []
for line in input_data:
    robot = list(map(int, re.findall(r"\d+|-\d+", line)))
    robot = ((robot[0], robot[1]), (robot[2], robot[3]))
    robots.append(robot)

most_connected_times = (0, 0)
for times in range(1, max_times + 1):
    moved_robot_positions = []
    vertical_fives = 0
    for robot in robots:
        moved_robot_positions.append(((robot[0][0] + robot[1][0] * times) % width, (robot[0][1] + robot[1][1] * times) % height))
    for robot in moved_robot_positions:
        if robot[1] + 5 < height:
            connected_count = 0
            for i in range(1, 6):
                if (robot[0], robot[1] + i) in moved_robot_positions:
                    connected_count += 1
                else:
                    break
            if connected_count == 5:
                vertical_fives += 1
    if vertical_fives > most_connected_times[1]:
        most_connected_times = (times, vertical_fives)
print(most_connected_times[0])