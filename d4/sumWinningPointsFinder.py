import re


def sum_winning_points_finder():
    # result
    value = 0

    file = open('input.txt', "r+")
    for line in file:
        ma = re.split('\|', line)
        p1 = re.findall('\d+', ma[0])
        p2 = re.findall('\d+', ma[1])
        p1.pop(0)

        winning_numbers = []
        for v in p2:
            if v in p1:
                winning_numbers.append(v)

        if len(winning_numbers) > 0:
            value += 2 ** (len(winning_numbers)-1)

    print(value)


if __name__ == '__main__':
    sum_winning_points_finder()
