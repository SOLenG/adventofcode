import re
from enum import Enum
from functools import cmp_to_key


class Hand(Enum):
    five_kind = 6
    four_kind = 5
    full_house = 4
    three_kind = 3
    two_pair = 2
    one_pair = 1
    high_card = 0


class Card(Enum):
    A = 14
    K = 13
    Q = 12
    J = 1
    T = 10


def sort(item, item2):
    hand = sort_by_type(item)
    hand2 = sort_by_type(item2)

    # sort by card if same type
    if hand == hand2:
        for i in range(5):
            c1 = item[0][i]
            c2 = item2[0][i]
            if c1 in Card._member_map_:
                c1 = Card.__members__[c1].value
            if c2 in Card._member_map_:
                c2 = Card.__members__[c2].value
            if int(c1) > int(c2):
                return 1
            if int(c1) < int(c2):
                return -1

    if hand > hand2:
        return +1
    if hand < hand2:
        return -1
    return 0


sort_cmp_key = cmp_to_key(sort)


def sort_by_type(item):
    hand = [item[0].count(c) for c in set(item[0])]
    # set a dict to find the J card and his count
    hand2 = {c: item[0].count(c) for c in set(item[0])}

    # update the hand array with J card data
    if 'J' in hand2:
        t = hand2['J']
        if t < 5:
            k = hand.index(t)
            hand.pop(k)
            k = hand.index(max(hand))
            hand[k] += t

    if 5 in hand:
        return Hand.five_kind.value
    if 4 in hand:
        return Hand.four_kind.value
    if 3 in hand:
        if 2 in hand:
            return Hand.full_house.value
        return Hand.three_kind.value

    if hand.count(2) == 2:
        return Hand.two_pair.value
    if 2 in hand:
        return Hand.one_pair.value

    return Hand.high_card.value


def winning_camel_finder():
    with open('input.txt', "r+") as f:
        result = 0
        data = []
        for line in f.readlines():
            data.extend([[str(x), int(y)] for x, y in re.findall(r'(.*)\s+(\d+)', line)])

        data.sort(key=sort_cmp_key)

        i = 1
        for datum in data:
            result += datum[1] * i
            i += 1

        # result
        print(result)


if __name__ == '__main__':
    winning_camel_finder()
