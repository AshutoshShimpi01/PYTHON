from loguru import logger
import logging
import math
logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
     datefmt="%Y-%m-%d %H:%M",
     level=logging.DEBUG
)



area = int(input("Enter value : "))

if(area<100):
    logger.info(f"Your value is less")
    logger.info("second line")
else:
    logger.info(f"Share more details")
    logger.info("third line")


Enter value : 111
2025-05-10 15:28:09.606 | INFO     | __main__:<module>:19 - Share more details
2025-05-10 15:28:09.607 | INFO     | __main__:<module>:20 - third line

Enter value : 11
2025-05-10 15:28:35.595 | INFO     | __main__:<module>:16 - Your value is less
2025-05-10 15:28:35.595 | INFO     | __main__:<module>:17 - second line
(base) ashutoshsanjayshimpi@192 PYTHON % 





from loguru import logger
import logging
import math
logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
     datefmt="%Y-%m-%d %H:%M",
     level=logging.DEBUG
)



area = int(input("Enter value : "))

if(area<100):
    logger.info(f"Your area is less")
    logger.info("second line")

elif area >100:
    logger.info(f"You can build 2 buld")
else:
    logger.info(f"Share more details")
    logger.info("third line")



