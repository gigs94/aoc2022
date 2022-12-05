#!/usr/bin/env python

import copy

testdata='''
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''

stack=[]
stack2=[]

def commands(l):
    return list(map(command,l.strip('\n').split('\n')))

def command(i):
    _,a,_,f,_,t=i.split(' ')
    return int(a),int(f)-1,int(t)-1

def restack9001(instruction):
    l=[]
    for i in range(instruction[0]):
        l.append(stack2[instruction[1]].pop())
    for i in range(len(l)):
        stack2[instruction[2]].append(l.pop())

def restack(instruction):
    for i in range(instruction[0]):
        stack[instruction[2]].append(stack[instruction[1]].pop())

def readstack(s):
    start=1
    step=4
    lines = s.strip('\n').split('\n')
    mll = max(map(len,lines))
    y=[]
    for i in range(start,mll,step):
        x=[]
        for j in lines:
            x.append(j[i])
        y.append(x)
    stacks=[]
    for i,z in enumerate(y):
        stacks.append([])
        for t in range(len(z)-2,-1,-1):
            if z[t] != ' ':
                stacks[i].append(z[t])
    return stacks


with open('day5.dat') as data:
    s,i = data.read().split('\n\n')
    #s,i= testdata.split('\n\n')
    stack = readstack(s)
    stack2 = copy.deepcopy(stack)
    instructions = commands(i)
    list(map(restack,instructions))
    list(map(restack9001,instructions))
    ans1=[ x.pop() for x in stack ]
    print(''.join(map(str,ans1)))
    ans2=[ x.pop() for x in stack2 ]
    print(''.join(map(str,ans2)))
