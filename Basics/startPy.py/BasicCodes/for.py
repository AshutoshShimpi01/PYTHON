from loguru import logger
import logging
import math
logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
     datefmt="%Y-%m-%d %H:%M",
     level=logging.DEBUG
)



numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8]  
  
a=0
for i in numbers:
    a=a+i
print("The sum of  is: ", a,i)     --62     and i gives total no. index 8






from loguru import logger
import logging
import math
logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
     datefmt="%Y-%m-%d %H:%M",
     level=logging.DEBUG
)



a = [3, 5, 6, 8, 4]  
for i in range( len( a ) ):  
    a.append(a[i] + 2)  
print( a ) 

[3, 5, 6, 8, 4, 5, 7, 8, 10, 6]    #same list + list+2  list append
