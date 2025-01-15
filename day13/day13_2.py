import re

def find_pushes(a_button, b_button, prize):
    if a_button[0] / b_button[0] == a_button[1] / b_button[1]: #in case slope of buttons is same
        if a_button[0] < b_button[0]:
            i = 0
            while difference > (0, 0):
                difference = (prize[0] - a_button[0] * i, prize[1] - a_button[1] * i)
                remainder = (difference[0] % b_button[0], difference[1] % b_button[1])
                if remainder == (0, 0):
                    return (i, difference[0] // b_button[0])
            i += 1
        else:
            i = 0
            while difference > (0, 0):
                difference = (prize[0] - b_button[0] * i, prize[1] - b_button[1] * i)
                if difference < 0:
                    break
                remainder = (difference[0] % a_button[0], difference[1] % a_button[1])
                if remainder == (0, 0):
                    return (i, difference[0] // a_button[0])
                i += 1
        return (0, 0)
    else:
        a = round((prize[0] - (b_button[0] / b_button[1]) * prize[1]) / (a_button[0] - (b_button[0] / b_button[1]) * a_button[1]))
        b = round((prize[0] - a * a_button[0]) / b_button[0])
        if a * a_button[0] + b * b_button[0] == prize[0] and a * a_button[1] + b * b_button[1] == prize[1]: #revised to check if both a and b are integers
            return (a, b)
        return (0, 0)

with open("input.txt", "r") as file:
    input_data = file.readlines()

a_buttons = []
b_buttons = []
prizes = []
for i in range(len(input_data) // 4):
    a_buttons.append(tuple(map(int, re.findall(r"\d+", input_data[i * 4]))))
    b_buttons.append(tuple(map(int, re.findall(r"\d+", input_data[i * 4 + 1]))))
    prizes.append(tuple(map(int, re.findall(r"\d+", input_data[i * 4 + 2]))))

total = 0
for i in range(len(prizes)):
    pushes = find_pushes(a_buttons[i], b_buttons[i], (prizes[i][0] + 10000000000000, prizes[i][1] + 10000000000000))
    total += pushes[0] * 3 + pushes[1]
print(total)