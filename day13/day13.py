import re

def find_pushes(a_button, b_button, prize):
    if a_button[0] / b_button[0] == a_button[1] / b_button[1]: #in case slope of buttons is same
        if a_button[0] < b_button[0]:
            for i in range(0, 101):
                difference = (prize[0] - a_button[0] * i, prize[1] - a_button[1] * i)
                if difference < 0:
                    break
                remainder = (difference[0] % b_button[0], difference[1] % b_button[1])
                if remainder == (0, 0):
                    return (i, difference[0] // b_button[0])
        else:
            for i in range(0, 101):
                difference = (prize[0] - b_button[0] * i, prize[1] - b_button[1] * i)
                if difference < 0:
                    break
                remainder = (difference[0] % a_button[0], difference[1] % a_button[1])
                if remainder == (0, 0):
                    return (i, difference[0] // a_button[0])
    elif round((prize[0] - (b_button[0] / b_button[1]) * prize[1]) / (a_button[0] - (b_button[0] / b_button[1]) * a_button[1])) == round((prize[0] - (b_button[0] / b_button[1]) * prize[1]) / (a_button[0] - (b_button[0] / b_button[1]) * a_button[1]), 10):
        a = round((prize[0] - (b_button[0] / b_button[1]) * prize[1]) / (a_button[0] - (b_button[0] / b_button[1]) * a_button[1]))
        b = int((prize[0] - a * a_button[0]) / b_button[0])
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

total_a = 0
total_b = 0
for i in range(len(prizes)):
    pushes = find_pushes(a_buttons[i], b_buttons[i], prizes[i])
    total_a += pushes[0]
    total_b += pushes[1]
    print(total_a * 3 + total_b)