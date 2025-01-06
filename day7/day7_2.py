import re

def do_operations(numbers):
    if(len(numbers) == 2):
        return (numbers[0] == numbers[1])
    sum = numbers[1] + numbers[2]
    sum_list = numbers[0:1] + numbers[3:]
    sum_list.insert(1, sum)
    if do_operations(sum_list):
        return True
    
    product = numbers[1] * numbers[2]
    product_list = numbers[0:1] + numbers[3:]
    product_list.insert(1, product)
    if do_operations(product_list):
        return True
    
    concat = int(str(numbers[1]) + str(numbers[2]))
    concat_list = numbers[0:1] + numbers[3:]
    concat_list.insert(1, concat)
    return do_operations(concat_list)

with open("input.txt", "r") as file:
    input_data = file.readlines()

all_numbers = []
total = 0
for i in range(len(input_data)):
    all_numbers.append(list(map(lambda a: int(a), re.findall(r"[0-9]+", input_data[i]))))
for numbers in all_numbers:
    if do_operations(numbers):
        total += numbers[0]
print(total)