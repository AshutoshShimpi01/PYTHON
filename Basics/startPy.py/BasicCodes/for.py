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


