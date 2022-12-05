#!/usr/bin/env python

from pandas import read_csv 
# 
# _,(a,b,c,d) = zip(*pd.read_csv('day4.dat', sep='[-,]', header=None, engine='python').items())
# print(((a<=c) & (d<=b) | (c<=a) & (b<=d)).sum(),
      # ((a<=d) & (d<=b) | (c<=b) & (b<=d)).sum())
# 
# exit()

def a(l : list):
    e= [ x.split('-') for x in l.split(',') ]
    r= [ set(range(int(x[0]),int(x[1])+1)) for x in e ]
    return r
    
def i(r : list):
    return r[0].issubset(r[1]) or r[1].issubset(r[0])
    
def c(r : list):
    return len(r[0].intersection(r[1])) > 0

with open('day4.dat') as data:
    lines = data.read().splitlines() 
    r=map(a,lines)
    print(sum(map(i,r)))
    #r=map(a,lines)
    print(sum(map(c,r)))