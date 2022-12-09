#!/usr/bin/env python

from collections import Counter

with open('day1.dat') as data:
    c={ int(i)+1:sum([int(x) for x in calories.strip().split('\n')]) for i,calories in enumerate(data.read().split('\n\n')) } 
    new_val = Counter(c).most_common(1)
    print(f'{new_val}, {sum([ x[1] for x in new_val])}')
    new_val = Counter(c).most_common(3)
    print(f'{new_val}, {sum([ x[1] for x in new_val])}')