#!/usr/bin/env python

from aocd import lines
from collections import namedtuple
from copy import deepcopy
import sys

sys.setrecursionlimit(2000)

coord = namedtuple("coord", ["x", "y"])

test = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def read(l):
    output = []
    for i in l:
        chars = []
        for j in i:
            chars.append(-ord(j))
        output.append(chars)
    return output


def search_all(s, s1, d):
    for a in d:
        if s in a:
            y = a.index(s)
        if s1 in a:
            y = a.index(s1)
        yield d.index(a), y


def search(s, d):
    for a in d:
        if s in a:
            y = a.index(s)
            break
    return d.index(a), y


def can_go(f, t):
    if f == -ord("E"):
        result = t == -ord("z") or t == -ord("y")
    else:
        result = t == -ord("S") or t <= f + 1
    return result


def can_move(new, prev, data):
    result = (
        new[0] >= 0
        and new[1] >= 0
        and new[0] < len(data)
        and new[1] < len(data[0])
        and not (new[0] == prev[0] and new[1] == prev[1])
    )
    return result


def trav(c: coord, e: int, steps: list, data: list, results: dict, prev: coord):
    # check results
    if c in results and len(steps) >= results[c]:
        return results
    else:
        results[c] = len(steps)

    if data[c[0]][c[1]] == e:
        if not "answer" in results or len(steps) < len(results["answer"]):
            results["answer"] = deepcopy(steps)
        return results

    for s in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        new = (c[0] + s[0], c[1] + s[1])
        if can_move(new, prev, data) and can_go(data[c[0]][c[1]], data[new[0]][new[1]]):
            steps.append(new)
            results = trav(new, e, steps, data, results, c)
            steps.pop()

    return results


class color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def printpath(path, data):
    for i, y in enumerate(data):
        for j, x in enumerate(y):
            if (i, j) in path:
                print(color.BOLD + color.GREEN + x + color.END, end="")
            else:
                print(color.BLUE + x + color.END, end="")
        print()


def go(d):
    data = read(d)
    end = -ord("S")
    start = search(-ord("E"), data)
    end_pos = search(-ord("S"), data)
    results = {}
    results = trav(start, end, [], data, results, start)
    printpath(results["answer"], d)
    print(results[end_pos], len(set(results["answer"])))


def go2(d):
    data = read(d)
    start = search(-ord("E"), data)

    final_answer = []
    for end in -ord("a"), -ord("S"):
        results = {}
        results = trav(start, end, [], data, results, start)
        if len(results["answer"]) < len(final_answer) or len(final_answer) == 0:
            final_answer = deepcopy(results["answer"])
    printpath(final_answer, d)
    print(len(final_answer))


go(test.splitlines())
go(lines)
go2(test.splitlines())
go2(lines)
# go(twelve_d.splitlines())
# go(lines)
