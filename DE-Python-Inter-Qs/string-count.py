from itertools import groupby

st = str(input('Enter a string : '))
output = ""

for key, group in groupby(st):
    # 1. Count: find the length of the current consecutive group
    count = len(list(group)) 
    
    # 2. Build: append the character (key) and its count
    output += key + str(count)

print(f"Output: {output}")








Step-by-Step Execution
for key, group in groupby(st):

The loop iterates over the output of groupby.

First Iteration ('a' group):

key is 'a'.

group contains the three consecutive 'a's.

list(group) converts this group into a list: ['a', 'a', 'a'].

count = len(['a', 'a', 'a']) sets count to 3.

output += 'a' + '3' makes output equal to 'a3'.

Second Iteration ('b' group):

key is 'b'.

group contains the two consecutive 'b's.

count = len(['b', 'b']) sets count to 2.

output += 'b' + '2' makes output equal to 'a3b2'.

Third Iteration ('c' group):

key is 'c'.

group contains the single 'c'.

count = len(['c']) sets count to 1.

output += 'c' + '1' makes output equal to 'a3b2c1'.
