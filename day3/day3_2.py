import re
# read input_data from file
with open("input.txt", "r") as file:
  input_data = file.readlines()

matches = []
total = 0
mult_active = True
for line in input_data:
  line_matches = re.findall(r"mul[(]\d{1,3},\d{1,3}[)]|do[(][)]|don't[(][)]", line)
  matches.extend(line_matches)
for match in matches:
  print(match)
  if(match == "do()"):
    mult_active = True
  elif(match == "don't()"):
    mult_active = False
  elif(mult_active):
    total += int(re.findall(r"\d{1,3}", match)[0]) * int(re.findall(r"\d{1,3}", match)[1])
print(total)