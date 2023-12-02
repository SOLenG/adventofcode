import re


def possible_game_finder():
    # color for alert
    red_alert = '\033[91m'
    end_alert = '\033[0m'
    green_alert = '\033[92m'
    # limit target we shouldn't exceed
    target = {'red': 12, 'green': 13, 'blue': 14}
    # result
    value = 0

    file = open('input.txt', "r+")
    for line in file:
        matches = re.search(r'Game (\d+):\s(.*)', line)
        if not matches:
            print('\033[91m Matches is empty \033[0m')
            continue

        failed = False
        game_set = matches[2].split(';')
        for gSet in game_set:
            details_matches = re.findall(r'(\d+)\s(\w+)', gSet)
            current_value = {'red': 0, 'green': 0, 'blue': 0}
            if not details_matches:
                continue

            for d in details_matches:
                current_value[d[1]] += int(d[0])
                if current_value[d[1]] > target[d[1]]:
                    failed = True
                    break
            else:
                continue
            break

        if not failed:
            value += int(matches[1])
            print('game : ' + matches[1] + green_alert + ' - succeed' + end_alert)
        else:
            print('games : ' + matches[1] + ' - red : ' + end_alert +
                  (green_alert, red_alert)[current_value['red'] > target['red']]
                  + str(current_value['red']) + '/' + str(target['red']) + end_alert + ' - green : ' + end_alert +
                  (green_alert, red_alert)[current_value['green'] > target['green']]
                  + str(current_value['green']) + '/' + str(target['green']) + end_alert + ' - blue : ' + end_alert +
                  (green_alert, red_alert)[current_value['blue'] > target['blue']]
                  + str(current_value['blue']) + '/' + str(target['blue']) + end_alert)

    print(value)


if __name__ == '__main__':
    possible_game_finder()
