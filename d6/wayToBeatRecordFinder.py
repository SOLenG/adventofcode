import re


def way_to_beat_record():
    with open('input.txt', "r+") as f:
        result = 1
        data = []
        for line in f.readlines():
            datum = re.findall(r'\d+', line)
            data.append([''.join(datum)])

        for i in range(len(data[0])):
            time = int(data[0][i])
            record = int(data[1][i])

            # calculation of loading time approximation
            approximation = int((time / 2) - int((time ** 2 / 4) / record * 10))

            # finding the exact approximation
            time_load_founded = False
            while not time_load_founded:
                time_travel = time - approximation
                distance = time_travel * approximation
                if distance > record:
                    # doesn't work in part 1, used to optimize the process
                    approximation -= ((distance-record)/distance) * approximation
                    continue
                elif distance <= record:
                    # doesn't work in part 1
                    approximation += ((distance-record)/distance) * approximation
                time_load_founded = True
            # calculation of the result
            result *= time - approximation * 2 + 1

        # result
        print(int(result))


if __name__ == '__main__':
    way_to_beat_record()
