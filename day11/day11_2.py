import re

dict = {}
def blink_count(times, stone):
    if (times, stone) in dict:
        return dict[times, stone]
    elif times == 0:
        return 1
    elif stone == 0:
        dict[times, stone] = blink_count(times - 1, 1)
        return dict[times, stone]
    elif len(str(stone)) % 2 == 0:
        dict[times, stone] = blink_count(times - 1, int(str(stone)[0:int(len(str(stone)) / 2)])) + blink_count(times - 1, int(str(stone)[int(len(str(stone)) / 2):]))
        return dict[times, stone]
    else:
        dict[times, stone] = blink_count(times - 1, stone * 2024)
        return dict[times, stone]

with open("input.txt", "r") as file:
    input_data = file.read()
all_stones = list(map(int, re.findall(r"\d+", input_data)))

total = 0
for stone in all_stones:
    total += blink_count(75, stone)
print(total)