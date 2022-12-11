#!/usr/bin/env python

from aocd import lines


dir = {"dirs": {"/": {"size": 0, "dirs": {}}}, "size": 0}
cwd = []


def ds():
    ptr = dir
    for i in cwd:
        ptr = ptr["dirs"][i]
    return ptr


def process(l):
    if l[0] == "$" and l[1] == "cd":
        if l[2] == "..":
            cwd.pop()
        else:
            cwd.append(l[2])
    elif l[0].isdigit():
        ds()["size"] += int(l[0])
    elif l[0] == "dir":
        ds()["dirs"][l[1]] = {"size": 0, "dirs": {}}
    else:
        pass


u100 = []
umax = []


def under100(d, x=0):
    for e in d["dirs"].keys():
        x += under100(d["dirs"][e])
    y = d["size"] + x
    if y < 100000:
        u100.append(y)
    umax.append(y)
    return y


list(map(process, [x.split(" ") for x in lines]))
total = under100(dir)
print(f"total: {total}")
print(f"answer1: {sum(u100)}")
print(umax)
needed = 30000000 - (70000000 - total)
answer = next(x for x in sorted(umax) if x > needed)
print(f"{needed=} {answer=}")
