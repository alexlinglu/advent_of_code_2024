import re

with open("input.txt", "r") as file:
    input_data = file.readlines()

left = []
right = []
for line in input_data:
    numbers = re.findall(r"\d+", line)
    left.append(numbers[0])
    right.append(numbers[1])

left.sort()
right.sort()
left.extend(right)

f = open("output.txt", "w")
for number in left:
    f.write(str(number) + "\n")