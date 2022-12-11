#!/usr/bin/env python

from collections import Counter
import numpy as np

'''
  X Y Z
A 4 8 3
B 1 5 9 
C 7 2 6

     L T W
rock 3 4 8
pape 1 5 9 
scis 2 6 7
'''

us=['X','Y','Z']
them=['A','B','C']
d=np.array([[4,8,3],[1,5,9],[7,2,6]])
d1=np.array([[3,4,8],[1,5,9],[2,6,7]])

#with open('day2.exp') as data:
with open('day2.dat') as data:
    # scores=[ x[1] for x in data.read().strip().split('\n') ] 
    dat = [ x.split() for x in data.read().strip().split('\n') ] 
    scores1=[ d[them.index(t)][us.index(u)] for t,u in dat ]
    scores2=[ d1[them.index(t)][us.index(u)] for t,u in dat ]
    print(f'part1: {sum(scores1)}')
    print(f'part2: {sum(scores2)}')