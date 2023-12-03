import re
from functools import reduce


def part_engine_finder():
    # result
    value = 0
    # init data's memories
    mem_line = {
        'current': {'number': {}, 'symbol': {}},
        'previous': {'number': {}, 'symbol': {}},
        'older': {'number': {}, 'symbol': {}}
    }

    file = open('input.txt', "r+")
    for line in file:
        # save previous data
        mem_line['older'] = mem_line['previous']
        # save previous data
        mem_line['previous'] = mem_line['current']
        # reinit current data
        mem_line['current'] = {'number': {}, 'symbol': {}}
        # find number position and value
        pos_number = re.compile('[0-9]+')
        for m in pos_number.finditer(line):
            mem_line['current']['number'][m.start()] = {'value': m.group(), 'span': m.span()}

        # find symbol position and data
        pos_symbol = re.compile('[*]')
        for m in pos_symbol.finditer(line):
            mem_line['current']['symbol'][m.start()] = {'value': m.group(), 'span': m.span()}

        # find value by symbol
        for ps in mem_line['previous']['symbol']:
            cs = mem_line['previous']['symbol'][ps]
            value += value_finder(cs, mem_line['current']['number'], mem_line['previous']['number'],
                                  mem_line['older']['number'])

    print(value)


def value_finder(cs, cns, pns, ons):
    possibility = []
    value = 0
    possibility += possibility_finder(cs, pns)
    possibility += possibility_finder(cs, cns)
    possibility += possibility_finder(cs, ons)

    if len(possibility) > 1:
        value += reduce((lambda x, y: x * y), possibility)

    return value


def possibility_finder(cs, ns):
    possibility = []
    for pn in ns:
        cn = ns[pn]
        if int(cs['span'][0]) >= int(cn['span'][0]) - 1 and int(cs['span'][1]) <= int(cn['span'][1]) + 1:
            possibility.append(int(cn['value']))

    return possibility


if __name__ == '__main__':
    part_engine_finder()
