#!/usr/bin/env python

def a(l : list):
    e= [ x.split('-') for x in l.split(',') ]
    r= [ set(range(int(x[0]),int(x[1])+1)) for x in e ]
    return r
    
def i(r : list):
    return r[0].issubset(r[1]) or r[1].issubset(r[0])
    
def c(r : list):
    s=r[0].intersection(r[1])
    return len(s) > 0

with open('day4.dat') as data:
    lines = data.read().splitlines() 
    r=map(a,lines)
    print(sum(map(i,r)))
    r=map(a,lines)
    print(sum(map(c,r)))