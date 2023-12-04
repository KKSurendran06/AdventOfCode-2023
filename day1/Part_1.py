import re

lines = []

while True:
    usr_input = input()
    if usr_input == '':
        break
    else:
        lines.append(usr_input)

algo = re.compile(r'[0-9]')

sums = 0

for item in lines:
    ob = algo.findall(item)       
    sums += int(ob[0]+ob[len(ob)-1])  

print(sums)        