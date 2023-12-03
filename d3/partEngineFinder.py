import re


def part_engine_finder():
    # result
    value = 0
    # init data's memories
    mem_line = {'current': {'number': {}, 'symbol': {}}, 'previous': {'number': {}, 'symbol': {}}}

    file = open('input.txt', "r+")
    for line in file:
        # save previous data
        mem_line['previous'] = mem_line['current']
        # reinit current data
        mem_line['current'] = {'number': {}, 'symbol': {}}
        # find number position and value
        pos_number = re.compile('[0-9]+')
        for m in pos_number.finditer(line):
            mem_line['current']['number'][m.start()] = {'value': m.group(), 'span': m.span()}

        # find symbol position and data
        pos_symbol = re.compile('[^0-9.\n ]')
        for m in pos_symbol.finditer(line):
            mem_line['current']['symbol'][m.start()] = {'value': m.group(), 'span': m.span()}

        # compare current symbol
        for ps in mem_line['current']['symbol']:
            cs = mem_line['current']['symbol'][ps]
            value += value_finder(cs, mem_line['current']['number'])
            value += value_finder(cs, mem_line['previous']['number'])

        # compare previous symbol
        for ps in mem_line['previous']['symbol']:
            cs = mem_line['previous']['symbol'][ps]
            value += value_finder(cs, mem_line['current']['number'])
    print(value)


def value_finder(cs, pns):
    value = 0
    for pn in pns:
        cn = pns[pn]
        if int(cs['span'][0]) >= int(cn['span'][0]) - 1 and int(cs['span'][1]) <= int(cn['span'][1]) + 1:
            value += int(cn['value'])

    return value


if __name__ == '__main__':
    part_engine_finder()
