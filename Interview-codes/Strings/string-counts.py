
from collections import *

st = input(str('Enter a string : '))
output = ''

counts = Counter(st)

for char, count in counts.items():
    output += char + str(count)
    
print(output)


Enter a string : aaabbc
a3b2c1
