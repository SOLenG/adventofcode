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
    with open('input.txt', "r+") as f:
        # find all seeds number
        seeds = [[int(x), int(y) + int(x) - 1] for x, y in re.findall('(\d+)\s(\d+)', f.readline().strip('\n'))]

        # create block data based on steps
        splitter = re.compile('\n\n.*:\n')
        blocks = splitter.split(f.read())
        # find all step's parameters (destination, source, range)
        data_map = []
        for i in range(len(blocks)):
            data_map.append([[int(x), int(y), int(z)] for x, y, z in re.findall('(\d+)\s(\d+)\s(\d+)', blocks[i])])

        # seeds are our starting positions range
        new_pos_r = seeds
        for step in Steps:
            # set new positions range for new search
            positions_range = new_pos_r
            new_pos_r = search_by_step(data_map[step.value], positions_range)

    # result
    print(min(new_pos_r)[0])


def search_by_step(data_map, positions):
    tmp = []
    # used to know when we are at the end of data_map
    i = 0
    for destination, source, delta in data_map:
        i += 1
        # ending of range of the source
        end = (source + delta - 1)
        # prepare the loop
        new_created = unchanged = positions
        tmp_unchanged = []
        while len(new_created) > 0:
            unchanged, changed, new_created = position_calculater(destination, end, source, new_created)
            if len(changed) > 0:
                tmp = tmp + changed
            if len(new_created) > 0 and len(unchanged) > 0:
                tmp_unchanged = unchanged

        positions = unchanged + tmp_unchanged

        # at the end of data_map, save all rest of the positions to prepare the return
        if i == len(data_map):
            tmp = unchanged + tmp + tmp_unchanged

    return tmp


# return the changed, unchanged, created positions ranges are found
def position_calculater(destination, end, source, positions):
    unchanged = []
    new_created = []
    changed = []
    for position in positions:
        # save unchanged position if it doesn't match
        if not ((source < position[0] or source in range(position[0], position[1] + 1)) and (
                (position[1]) <= end or end in range(position[0], position[1] + 1))):
            unchanged = unchanged + [position]
            continue

        # else processing
        # create position array of inner and outer position manage by the step
        new_position = []
        current_position = []
        if source > position[0]:
            new_position.append([position[0], source - 1])
            current_position.append(source)
        else:
            current_position.append(position[0])
        if end < position[1]:
            new_position.append([end + 1, position[1]])
            current_position.append(end)
        else:
            current_position.append(position[1])

        # update inner position by the step
        current_position[0] = current_position[0] - source + destination
        current_position[1] = current_position[1] - source + destination

        # update position of outer in collision with inner new position
        if len(new_position) > 0 and current_position[0] in new_position[0]:
            new_position[0][0] = new_position[0][0] - source + current_position[1]
            new_position[0][1] = new_position[0][1] - source + current_position[1]
        if len(new_position) > 1 and current_position[1] in new_position[1]:
            new_position[1][0] = new_position[1][0] - source + current_position[1]
            new_position[1][1] = new_position[1][1] - source + current_position[1]

        # save changed and new position created
        changed = changed + [current_position]
        if new_position:
            new_created.extend(new_position)

    return unchanged, changed, new_created


if __name__ == '__main__':
    farm_optimization_finder()
