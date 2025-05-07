print("Hello")


**#using f string
name = 10
print(f"my name is {name} thanks")
#my name is 10 thanks

name = 10
a=20
b=30
print(f"my name is {name} {a} {b}")

#my name is 10 20 30


--------------------------

**#USING .FORMAT
name = 10
print("my self is {}" .format(name))
#my self is 10


name = 10
a=20
b=30
print("my self is {} {} {}" .format(name,a,b))
#my self is 10 20 30


----------------------------

**LOGGING.info


name = 10
a=20
b=30
print(f"my name is {name} {a} {b}")


from loguru import logger

import logging

logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
     datefmt="%Y-%m-%d %H:%M",
     level=logging.DEBUG
)

logging.info(f"my name is {name} {a} {b}")

logger.info(f"my name is {name} {a} {b}")


my name is 10 20 30
2025-05-07 22:48 - INFO - my name is 10 20 30
2025-05-07 22:48:36.262 | INFO     | __main__:<module>:20 - my name is 10 20 30
