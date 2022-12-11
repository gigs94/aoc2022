#!/usr/bin/env python

from aocd import lines
import numpy as np

test = """30373
25512
65332
33549
35390"""


def up(f, x, y):
    me = f[x][y]
    for a in range(y - 1, -1, -1):
        if f[x][a] >= me:
            return False
    return True


def down(f, x, y):
    me = f[x][y]
    for a in range(y + 1, len(f[:][0])):
        if f[x][a] >= me:
            return False
    return True


def left(f, x, y):
    me = f[x][y]
    for a in range(x - 1, -1, -1):
        if f[a][y] >= me:
            return False
    return True


def right(f, x, y):
    me = f[x][y]
    for a in range(x + 1, len(f[0])):
        if f[a][y] >= me:
            return False
    return True


def ssup(f, x, y):
    me = f[x][y]
    count = 0
    for a in range(y - 1, -1, -1):
        count += 1
        if f[x][a] >= me:
            break
    return count


def ssdown(f, x, y):
    count = 0
    me = f[x][y]
    for a in range(y + 1, len(f[:][0])):
        count += 1
        if f[x][a] >= me:
            break
    return count


def ssleft(f, x, y):
    me = f[x][y]
    count = 0
    for a in range(x - 1, -1, -1):
        count += 1
        if f[a][y] >= me:
            break
    return count


def ssright(f, x, y):
    me = f[x][y]
    count = 0
    for a in range(x + 1, len(f[0])):
        count += 1
        if f[a][y] >= me:
            break
    return count


t = np.array(test.splitlines())


def walk(f):
    count = 0
    for x in range(len(f[0])):
        for y in range(len(f[:][0])):
            z = any([left(f, x, y), right(f, x, y), up(f, x, y), down(f, x, y)])
            count += z
    return count


def sswalk(f):
    max = 0
    for x in range(len(f[0])):
        for y in range(len(f[:][0])):
            z = ssleft(f, x, y) * ssright(f, x, y) * ssup(f, x, y) * ssdown(f, x, y)
            max = z if z > max else max
    return max


print(walk(t))
print(walk(lines))
print(sswalk(t))
print(sswalk(lines))
