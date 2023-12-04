import re


def sum_winning_points_finder():
    # result
    value = 0
    next_scratchcard_copy_available = {}
    file = open('input.txt', "r+")
    for line in file:
        ma = re.split('\|', line)
        p1 = re.findall('\d+', ma[0])
        p2 = re.findall('\d+', ma[1])
        card_number = p1.pop(0)

        # original scratchcard
        value += 1
        # find winning numbers
        winning_numbers = []
        for v in p2:
            if v in p1:
                winning_numbers.append(v)

        loop = 1
        # add all current number card scratchcard found
        if next_scratchcard_copy_available.get(card_number):
            value += next_scratchcard_copy_available[card_number]
            loop += next_scratchcard_copy_available[card_number]

        # update all the number of all copy of scratchcard win
        if len(winning_numbers) > 0:
            for x in range(len(winning_numbers)):
                key = str(int(card_number) + x + 1)
                if not next_scratchcard_copy_available.get(key):
                    next_scratchcard_copy_available[key] = 0
                next_scratchcard_copy_available[key] += loop
    print(value)


if __name__ == '__main__':
    sum_winning_points_finder()
