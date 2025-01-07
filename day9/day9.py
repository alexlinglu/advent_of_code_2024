import math

def compact(disk):
    while "." in disk:
        disk[disk.index(".")] = disk[-1]
        disk.pop()
        while disk[-1] == ".":
            disk.pop()
    return disk

with open("input.txt", "r") as file:
    input_data = file.readline()

blocks = []
total = 0 
for i in range(len(input_data)):
    if i % 2 == 0:
        for j in range(int(input_data[i])):
            blocks.append(math.floor(i / 2))
    else:
        for j in range(int(input_data[i])):
            blocks.append(".")

compacted_disk = compact(blocks)
for k in range(len(compacted_disk)):
    total += k * compacted_disk[k]
print(total)