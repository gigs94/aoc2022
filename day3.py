#!/usr/bin/env python

from collections import Counter

a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def priority(x : Counter):
    return [ a.index(i)+1 for i in x.keys() ][0]

def read(lines):
    for line in lines:
        x=Counter(line[0:len(line)//2])
        y=Counter(line[len(line)//2:])
        z=(x & y)
        yield priority(z)

def read2(lines):
    for i in range(0,len(lines),3):
        x=Counter(lines[i])&Counter(lines[i+1])&Counter(lines[i+2])
        yield(priority(x))

with open('day3.dat') as data:
    lines = data.read().splitlines() 
    print(f'problem1: {sum(read(lines))}')
    print(f'problem2: {sum(read2(lines))}')