import re

with open("input.txt", "r") as file:
  input_data = file.readlines()

matches = []
total = 0
for line in input_data:
  line_matches = re.findall(r"mul[(]\d{1,3},\d{1,3}[)]", line)
  matches.extend(line_matches)
for match in matches:
  print(match)
  total += int(re.findall(r"\d{1,3}", match)[0]) * int(re.findall(r"\d{1,3}", match)[1])
print(total)