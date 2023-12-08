import re
from enum import Enum


class direction(Enum):
    L = 0
    R = 1


def path_camel_finder():
    with open('input.txt', "r+") as f:
        value = 0
        road = {}
        instruction = re.findall(r'(.*)', f.readline())[0]
        f.readline()
        for line in f.readlines():
            datum = {x: (y, z) for x, y, z in re.findall(r'(.*)\s=\s\((.*),\s(.*)\)', line)}
            road.update(datum)

        path_current = 'AAA'
        destination_reached = False
        while not destination_reached:
            for c in instruction:
                path_current = road[path_current][direction.__members__[c].value]
                value += 1
                if path_current == 'ZZZ':
                    destination_reached = True
                    break

        # result
        print(value)


if __name__ == '__main__':
    path_camel_finder()
