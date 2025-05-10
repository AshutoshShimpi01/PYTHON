from loguru import logger
import logging
logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
     datefmt="%Y-%m-%d %H:%M",
     level=logging.DEBUG
)

len_land=100
br_land=100
total_a= len_land * br_land

logger.info(f"the total area of land is {total_a} sq ft")

#2025-05-10 14:25:06.929 | INFO     | __main__:<module>:14 - the total area of land is 10000 sq ft
