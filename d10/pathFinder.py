# direction
RIGHT = 1 << 0
LEFT = 1 << 1
TOP = 1 << 2
BOTTOM = 1 << 3
# no direction (for the tile without pipe)
EMPTY = 1 << 5
# position of the beast
BEAST = 1 << 4

tile = {
    "7": LEFT | BOTTOM,
    "F": RIGHT | BOTTOM,
    "J": TOP | LEFT,
    "L": TOP | RIGHT,
    "-": LEFT | RIGHT,
    "|": TOP | BOTTOM,
    "S": TOP | RIGHT | BOTTOM | LEFT | BEAST,
    ".": EMPTY
}


class Cell(object):
    def __init__(self, name, row, col):
        self.name = name
        self.row = row
        self.col = col

        # set adjacent tile
        self.neighbors: list[dict[row:str, col:str]] = []
        if tile[name] & TOP:
            self.neighbors.append({"row": row - 1, "col": col})
        if tile[name] & BOTTOM:
            self.neighbors.append({"row": row + 1, "col": col})
        if tile[name] & RIGHT:
            self.neighbors.append({"row": row, "col": col + 1})
        if tile[name] & LEFT:
            self.neighbors.append({"row": row, "col": col - 1})

    def __repr__(self):
        return str(self.name)


class Map(object):
    def __init__(self):
        self.cells = {}
        self.start: Cell | None = None
        self.position: Cell | None = None
        self.previous_position: Cell | None = None

    def add_cell(self, **cell):
        if not self.cells.get(cell['row']):
            self.cells[cell['row']] = {}
        self.cells[cell['row']][cell['col']] = Cell(cell['name'], cell['row'], cell['col'])

        if cell['name'] == 'S':
            self.position = self.start = self.cells[cell['row']][cell['col']]

    def move(self):
        # all tiles have a maximum of 2 directions, one direction is your previous position, so we take the second
        if self.position.neighbors[0]['row'] == self.previous_position.row and self.position.neighbors[0][
            'col'] == self.previous_position.col:
            self.previous_position = self.position
            self.position = self.cells[self.position.neighbors[1]['row']][self.position.neighbors[1]['col']]
        else:
            self.previous_position = self.position
            self.position = self.cells[self.position.neighbors[0]['row']][self.position.neighbors[0]['col']]

        return self.position

    # travels the entire loop to determine the maximum distance from the furthest position from the beast
    def run_away(self):
        # fix BEAST, he has 4 direction, but the pipe has a maximum 2 directions
        for neighbor in self.start.neighbors:
            if not self.cells.get(neighbor['row']) or not self.cells[neighbor['row']].get(neighbor['col']):
                continue
            cell = self.cells[neighbor['row']][neighbor['col']]

            # remove the wrong direction
            if not [x for x in cell.neighbors if x['row'] == self.start.row and x['col'] == self.start.col]:
                self.start.neighbors.remove(neighbor)
        self.previous_position = self.cells[self.start.neighbors[0]['row']][self.start.neighbors[0]['col']]

        step = 1
        while self.move() != self.start:
            step += 1
        return int(step / 2)


def path_finder() -> None:
    with open('input.txt', "r+") as f:
        map = Map()
        i = 0
        for line in f.readlines():
            j = 0
            for c in line:
                if c == '\n':
                    break
                map.add_cell(name=c, row=i, col=j)
                j += 1

            i += 1

        # result
        print(map.run_away())


if __name__ == '__main__':
    path_finder()
