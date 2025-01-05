import re
import math

with open("input.txt", "r") as file:
  input_data = file.readlines()

def checkOrder(update, rules):
    for k in range(len(update)):
        for Key, Value in rules:
            if Key == update[k] and Value in update[0:k]:
                return False
    return True

total = 0
rules = []
for i in range(1176):
  rules.append((input_data[i][0:2], input_data[i][3:5]))
for j in range(190):
  update =  re.findall(r"\d\d", input_data[j + 1177])
  if(checkOrder(update, rules)):
    total += int(update[math.floor(len(update) / 2)])
print(total)