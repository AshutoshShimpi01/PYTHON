from loguru import logger
import logging
import math
logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
     datefmt="%Y-%m-%d %H:%M",
     level=logging.DEBUG
)

len = input("enter len of land : ")
br = input("br of lanf : ")
area = int(len) *int(br)

logger.info(f"Area of land is {area} sq ft" )


enter len of land : 10
br of lanf : 10
2025-05-10 14:59:51.641 | INFO     | __main__:<module>:15 - Area of land is 100 sq ft
