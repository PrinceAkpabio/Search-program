# Combining, Searching and Extracting in Regular Expressions

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
       print(x)

# Escape Character

import re

x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)