from aocd import lines
from collections import Counter

#lines=['bvwbjplbgvbhsrlpgdmjqwftvncz']
#lines=['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg']
somm = [ len(Counter(lines[0][p:p+14])) for p in range(len(lines[0])-14) ]
sopm = [ len(Counter(lines[0][p:p+4])) for p in range(len(lines[0])-3) ]

print(sopm.index(4)+4)
print(somm.index(14)+4)