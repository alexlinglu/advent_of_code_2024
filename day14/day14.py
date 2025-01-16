import re

with open("input.txt", "r") as file:
    input_data = file.readlines()

width = 101
height = 103
times = 100
robots = []
for line in input_data:
    robot = list(map(int, re.findall(r"\d+|-\d+", line)))
    robot = ((robot[0], robot[1]), (robot[2], robot[3]))
    robots.append(robot)

first_q = 0
second_q = 0
third_q = 0
fourth_q = 0
for robot in robots:
    robot = (((robot[0][0] + robot[1][0] * times) % width, (robot[0][1] + robot[1][1] * times) % height), robot[1])
    if robot[0][0] > width // 2 and robot[0][1] < height // 2:
        first_q += 1
    elif robot[0][0] < width // 2 and robot[0][1] < height // 2:
        second_q += 1
    elif robot[0][0] < width // 2 and robot[0][1] > height // 2:
        third_q += 1
    elif robot[0][0] > width // 2 and robot[0][1] > height // 2:
        fourth_q += 1
print(first_q * second_q * third_q * fourth_q)