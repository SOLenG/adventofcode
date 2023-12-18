import re


class Node(object):
    def __init__(self, value: int):
        self.value = value

    def __sub__(self, node):
        assert isinstance(node, Node)
        return self.value - node.value

    def __add__(self, node):
        assert isinstance(node, Node)
        return self.value + node.value

    def __radd__(self, node):
        assert isinstance(node, int)
        return self.value + node


class Tree(object):
    def __init__(self, nodes: list[int]):
        self.nodes: dict[int, list[Node]] = {0: [Node(int(v)) for v in nodes]}

    # calculating of all differential values between adjacent nodes and adding the value into the tree
    def build(self):
        diff = []
        i = len(self.nodes) - 1

        for x in range(int(len(self.nodes[i]) - 1)):
            v = self.nodes[i][x:x + 2]
            diff.append(v[1] - v[0])

        self.nodes[i + 1] = [Node(int(v)) for v in diff]
        if len(set(diff)) != 1:
            self.build()

    # find the next value of the tree
    def next_value(self):
        value = 0
        for n in reversed(self.nodes):
            value += self.nodes[n][-1]

        return value


def environmental_instability_finder() -> None:
    with open('input.txt', "r+") as f:
        value = 0
        trees = []
        for line in f.readlines():
            datum = re.findall(r'(-?\d+)', line)
            trees.append(Tree(datum))

        # generating of the tree and get the next value
        for tree in trees:
            tree.build()
            value += tree.next_value()

        # result
        print(value)


if __name__ == '__main__':
    environmental_instability_finder()
