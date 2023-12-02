import re


def possible_game_finder():
    # result
    value = 0

    file = open('input.txt', "r+")
    for line in file:
        matches = re.search(r'Game (\d+):\s(.*)', line)
        if not matches:
            print('\033[91m Matches is empty \033[0m')
            continue

        current_value = {'red': 0, 'green': 0, 'blue': 0}
        game_set = matches[2].split(';')
        for gSet in game_set:
            details_matches = re.findall(r'(\d+)\s(\w+)', gSet)
            if not details_matches:
                continue

            for d in details_matches:
                if current_value[d[1]] < int(d[0]):
                    current_value[d[1]] = int(d[0])

        value += current_value['red'] * current_value['green'] * current_value['blue']
        print('games : ' + matches[1] + ' - red : ' + str(current_value['red'])
              + ' - green : ' + str(current_value['green'])
              + ' - blue : ' + str(current_value['blue']))

    print(value)


if __name__ == '__main__':
    possible_game_finder()
