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
else:
    logger.info(f"Share more details")


2025-05-10 15:23:36.579 | INFO     | __main__:<module>:16 - Your value is less
2025-05-10 15:23:48.104 | INFO     | __main__:<module>:18 - Share more details
