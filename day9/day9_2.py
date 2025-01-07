import math

with open("input.txt", "r") as file:
    input_data = file.readline()

def compact2(disk):
    i = len(disk) - 1
    while i > 0:
            if disk[i][0] != ".":
                for j in range(i):
                    if disk[j][0] == "." and disk[j][1] >= disk[i][1]: #works much better with >=
                        #combine blanks
                        i_fix = 0
                        if i != len(disk) - 1:
                            disk[i - 1] = (".", disk[i - 1][1] + disk[i][1] + disk[i + 1][1])
                            disk.pop(i + 1)
                        else:
                            disk[i - 1] = (".", disk[i - 1][1] + disk[i][1])
                            i_fix = -1

                        temp = disk.pop(i)
                        disk.insert(j + 1, (".", disk[j][1] - temp[1])) #add empty blanks to keep file-space pattern
                        disk[j] = temp
                        disk.insert(j, (".", 0))
                        i += 2 + i_fix
                        break
            i -= 1
    return disk

blocks = []
total = 0 
for i in range(len(input_data)):
    if i % 2 == 0:
        blocks.append((math.floor(i / 2), int(input_data[i])))
    else:
        blocks.append((".", int(input_data[i])))
compacted_disk = compact2(blocks)

disk = []
for i in range(len(compacted_disk)):
    expanded_block = [compacted_disk[i][0]] * compacted_disk[i][1]
    disk.extend(expanded_block)

for i in range(len(disk)):
    if disk[i] != ".":
        total += i * disk[i]
print(total)