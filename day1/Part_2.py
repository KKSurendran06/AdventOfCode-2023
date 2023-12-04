import re
from word2number import w2n

lines = []

while True:
    usr_input = input()
    if usr_input == '':
        break
    else:
        lines.append(usr_input)

algo = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))')

sums = 0

for item in lines:
    ob = algo.findall(item)     
    convertNos = (w2n.word_to_num(ob[0]))*10+w2n.word_to_num(ob[len(ob)-1])
    sums += convertNos
print(sums)    

