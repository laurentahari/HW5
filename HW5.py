Lauren Tahari
newest additon

import re

total= 0
number = 0
f = open('regex_sum_38192.txt')
for line in f:
    num = re.findall("[0-9]+", line)
    for i in num:
        number = number +int(i)
    total = total + number
    number = 0
print (total)
