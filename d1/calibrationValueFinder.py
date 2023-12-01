import re

def calibrationValueFinder():
    value = 0
    file = open('input.txt', "r+")
    for line in file:
        matches = re.search(r"(\d).*(\d)|(\d)[a-zA-Z]*", line)
        if not matches:
            continue

        if matches[2]:
            value += int(matches[1] + matches[2])
            print("2 values : " + matches[1] + matches[2])
        else:
            value += int(matches[3] + matches[3])
            print("1 values : " + matches[3] + matches[3])

    print(value)


if __name__ == '__main__':
    calibrationValueFinder()