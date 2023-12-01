import re

rPattern = r'''\s*
(?(DEFINE)
  (?<one_to_9>
  (?:f(?:ive|our)|s(?:even|ix)|t(?:hree|wo)|(?:ni|o)ne|eight)
  )
  (?<zero_to_9>
  (?&one_to_9)|zero
  )
)
((?&zero_to_9)|\d).*(\d|(?&zero_to_9))|(\d|(?&zero_to_9))[a-zA-Z]*
'''

numberSpelled = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def converToNumber(match):
    for idx, word in enumerate(numberSpelled):
        if match == word:
            return str(idx)
    return match


def calibrationValueFinder():
    value = 0
    file = open('input.txt', "r+")
    for line in file:
        matches = re.search(
            r'((?:f(?:ive|our)|s(?:even|ix)|t(?:hree|wo)|(?:ni|o)ne|eight)|zero|\d).*(\d|(?:f(?:ive|our)|s(?:even|ix)|t(?:hree|wo)|(?:ni|o)ne|eight)|zero)|(\d|(?:f(?:ive|our)|s(?:even|ix)|t(?:hree|wo)|(?:ni|o)ne|eight)|zero)[a-zA-Z]*',
            line)
        if not matches:
            continue

        if matches[2]:
            value += int(converToNumber(matches[1]) + converToNumber(matches[2]))
            print("2 values : " + matches[1] + matches[2])
        else:
            value += int(converToNumber(matches[3]) + converToNumber(matches[3]))
            print("1 values : " + matches[3] + matches[3])

    print(value)


if __name__ == '__main__':
    calibrationValueFinder()
