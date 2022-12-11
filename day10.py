#!/usr/bin/env python

from aocd import lines

test = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

test2 = """noop
addx 3
addx -5"""


signals = {}
crt = []


def engine(c, x, s, a):
    # DURING CYCLE
    signals[c] = c * x
    crt.append("#" if abs((c % 40) - s) <= 1 else " ")
    c += 1
    # AFTER CYCLE
    if a:
        x += int(a)
    s = x
    return c, x, s


def process(lines):
    l = [l.split() for l in lines]
    c = 0
    x = 1
    s = x
    for m in l:
        if m[0] == "noop":
            c, x, s = engine(c, x, s, None)
        elif m[0] == "addx":
            c, x, s = engine(c, x, s, None)
            c, x, s = engine(c, x, s, m[1])

    # c, x, s = engine(c, x, s, None)


process(test.splitlines())
sigs = [20, 60, 100, 140, 180, 220]
print(sum([signals[x] for x in sigs]))
crt2 = "".join(crt)
for i in [crt2[i : i + 40] for i in range(0, len(crt2), 40)]:
    print(i)
crt = []
process(lines)
print(sum([signals[x] for x in sigs]))
crt2 = "".join(crt)
for i in [crt2[i : i + 40] for i in range(0, len(crt2), 40)]:
    print(i)
