import re
from enum import Enum


class Direction(Enum):
    L = 0
    R = 1


def path_camel_finder() -> None:
    with open('input.txt', "r+") as f:
        # get instruction of navigation
        instructions = re.findall(r'(.*)', f.readline())[0]
        # skip the empty line 2
        f.readline()
        # get all steps and starting position of the paths
        steps = {}
        start_paths = []
        for line in f.readlines():
            datum = re.findall(r'(.*)\s=\s\((.*),\s(.*)\)', line)[0]
            steps.update({datum[0]: (datum[1], datum[2])})

            if 'A' in datum[0]:
                start_paths.append(datum[0])

        # find the count of steps before the path reaches its end
        destination_reached_counter = get_number_steps_for_each_paths(instructions, start_paths, steps)

        # result
        print(get_least_common_multiple_of_each_numbers(destination_reached_counter))


def get_number_steps_for_each_paths(instructions: dict[str], start_paths: list[str], steps) -> list[int]:
    destination_reached_counter: list[int] = []
    for path in start_paths:
        counter: int = 0
        while True:
            destination_reached = False
            for instruction in instructions:
                counter += 1
                path, destination_reached = next_step(instruction, path, steps)
                if destination_reached:
                    destination_reached_counter.append(counter)
                    break
            if destination_reached:
                break

    return destination_reached_counter


def get_least_common_multiple_of_each_numbers(numbers) -> int:
    lcm: int = 1
    for number in numbers:
        lcm = get_least_common_multiple(lcm, number)

    return lcm


def get_least_common_multiple(a, b) -> int:
    return int((a * b) / greatest_common_divisor(a, b))


def greatest_common_divisor(a, b) -> int:
    if b == 0:
        return a
    r = a % b

    return greatest_common_divisor(b, r)


def next_step(instruction, path_current, road) -> tuple[str, bool]:
    destination_reached: bool = False
    path_new = road[path_current][Direction.__members__[instruction].value]
    if 'Z' in path_new:
        destination_reached = True
    return path_new, destination_reached


if __name__ == '__main__':
    path_camel_finder()
