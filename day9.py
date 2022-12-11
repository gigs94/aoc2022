#!/usr/bin/env python

from aocd import lines
import copy

test = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

test2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


class pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def adjacent(self, other):
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

    def is_diagonal(self):
        return abs(self.x) + abs(self.y) == 2

    def move(self, other):
        if self.adjacent(other):
            return
        else:
            (xdiff, ydiff) = (other.x - self.x, other.y - self.y)
            if abs(xdiff) < 2 and abs(ydiff) == 2:
                self.x = other.x
                self.add(pos(0, 1)) if ydiff == 2 else self.add(pos(0, -1))
            elif abs(ydiff) < 2 and abs(xdiff) == 2:
                self.y = other.y
                self.add(pos(1, 0)) if xdiff == 2 else self.add(pos(-1, 0))
            elif abs(xdiff) == 2 and abs(ydiff) == 2:
                self.add(pos(xdiff // 2, ydiff // 2))

    def direction(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return pos(x, y)

    def add(self, other):
        self.x += other.x
        self.y += other.y

    def set(self, other):
        self.x = other.x
        self.y = other.y

    def coord(self):
        return (self.x, self.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"


h_changer = {"R": pos(1, 0), "L": pos(-1, 0), "U": pos(0, 1), "D": pos(0, -1)}


def mover(move, knots):
    prev = copy.deepcopy(knots)
    knots[0].add(move)
    for i in range(1, len(knots)):
        knots[i].move(knots[i - 1])
        # if not knots[i].adjacent(knots[i - 1]):
        # direc = knots[i].direction(prev[i - 1])
        # if direc.is_diagonal():
        # knots[i].add(direc)
        # else:
        # knots[i].set(prev[i - 1])


def print_knots(knots, bh):
    minx, miny, maxx, maxy = gridsize(test2.splitlines())
    coords = [a.coord() for a in knots]

    # print(minx, miny, maxx, maxy)
    shift = (-minx, -miny)
    cols = maxx + 1 - minx
    rows = maxy + 1 - miny
    z = [["."] * cols] * rows

    for y in range(maxy, miny - 1, -1):
        for x in range(minx, maxx):
            if (x, y) in coords:
                print(coords.index((x, y)), end="")
            elif (x, y) == (0, 0):
                print("s", end="")
            elif (x, y) in bh:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print("===================")


def niner(lst: list):
    prev = None
    knots = [
        pos(0, 0),
        pos(0, 0),
        pos(0, 0),
        pos(0, 0),
        pos(0, 0),
        pos(0, 0),
        pos(0, 0),
        pos(0, 0),
        pos(0, 0),
        pos(0, 0),
    ]

    been_here = [knots[len(knots) - 1].coord()]
    for l in [l.split() for l in lst]:
        for i in range(int(l[1])):
            mover(h_changer[l[0]], knots)
            been_here.append(knots[len(knots) - 1].coord())
            # print_knots(knots, been_here)
    return len(set(been_here))


def somer(lst: list):
    prev = None
    h_xy = pos(0, 0)
    t_xy = pos(0, 0)
    been_here = [t_xy.coord()]
    move = False
    for l in [l.split() for l in lst]:
        prev = copy.deepcopy(h_xy)
        for i in range(int(l[1])):
            h_xy.add(h_changer[l[0]])
            if not h_xy.adjacent(t_xy):
                been_here.append(prev.coord())
                t_xy = copy.deepcopy(prev)
            prev = copy.deepcopy(h_xy)
    return len(set(been_here))


def gridsize(t):
    maxx, maxy, minx, miny = 0, 0, 0, 0
    xy = pos(0, 0)
    for x in t:
        l = x.split()
        if l[0] == "R":
            xy.add(pos(int(l[1]), 0))
            maxx = max(xy.coord()[0], maxx)
        if l[0] == "L":
            xy.add(pos(-int(l[1]), 0))
            minx = min(xy.coord()[0], minx)
        if l[0] == "U":
            xy.add(pos(0, int(l[1])))
            maxy = max(xy.coord()[1], maxy)
        if l[0] == "D":
            xy.add(pos(0, -int(l[1])))
            miny = min(xy.coord()[1], miny)
    return minx, miny, maxx, maxy


print(somer(test.splitlines()))
print(somer(lines))
print(niner(test.splitlines()))
print(niner(test2.splitlines()))
print(niner(lines))
