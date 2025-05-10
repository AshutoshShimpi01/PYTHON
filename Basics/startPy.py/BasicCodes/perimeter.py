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
perimeter_land = 2 * (len_land + br_land)

logger.info(f"perimeter of land is {perimeter_land}" )

#2025-05-10 14:32:42.489 | INFO     | __main__:<module>:18 - perimeter of land is 400
