import re
import sys
sys.setrecursionlimit(100000)

def blink(stones):
    if(len(stones) == 0):
        return stones
    elif stones[0] == 0:
        one_stone = [1]
        one_stone.extend(blink(stones[1:]))
        return one_stone
    elif len(str(stones[0])) % 2 == 0:
        two_stone = [int(str(stones[0])[0:int(len(str(stones[0])) / 2)]), int(str(stones[0])[int(len(str(stones[0])) / 2):])]
        two_stone.extend(blink(stones[1:]))
        return two_stone
    else:
        three_stone = [stones[0] * 2024]
        three_stone.extend(blink(stones[1:]))
        return three_stone
    
def blink_times(times, stones):
    if times == 0:
        return stones
    else:
        return blink_times(times - 1, blink(stones))

with open("input.txt", "r") as file:
    input_data = file.read()
all_stones = list(map(int, re.findall(r"\d+", input_data)))

stone_count = 0
for stone in all_stones:
    stone_count += len(blink_times(25, [stone]))
print(stone_count)