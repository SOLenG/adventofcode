import re
from enum import Enum


class Steps(Enum):
    SEED_TO_SOIL = 0
    SOIL_TO_FERTILIZER = 1
    FERTILIZER_TO_WATER = 2
    WATER_TO_LIGHT = 3
    LIGHT_TO_TEMPERATURE = 4
    TEMPERATURE_TO_HUMIDITY = 5
    HUMIDITY_TO_LOCATION = 6


def farm_optimization_finder():
    # result
    value = 0
    with open('input.txt', "r+") as f:
        # find all seeds number
        seeds = [int(x) for x in re.findall('\d+', f.readline().strip('\n'))]
        # create block data based on steps
        splitter = re.compile('\n\n.*:\n')
        blocks = splitter.split(f.read())
        # find all step's parameters (destination, source, range)
        data_map = []
        for i in range(len(blocks)):
            data_map.append([[int(x), int(y), int(z)] for x, y, z in re.findall('(\d+)\s(\d+)\s(\d+)', blocks[i])])

        # for all seeds, get new position by through steps
        for seed in seeds:
            position = seed
            for step in Steps:
                for destination, source, delta in data_map[step.value]:
                    if source <= position <= (source + delta - 1):
                        position = position - source + destination
                        break
            # new value if the new position is lower
            # position 0 is not possible and is used to detect the first initialization
            if value > position or value == 0:
                value = position
    print(value)


if __name__ == '__main__':
    farm_optimization_finder()
