#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

from math import lcm
# so I don't have any more accidentally global internal loop variables...
def main():
    rl = input()
    input()
    nodes = {}
    currents = []
    for line in slorp():
        f, lr = line.split(' = ')
        nodes[f] = lr[1:-1].split(', ')
        if f[-1] == 'A':
            currents.append(f)
    
    def aaa(current):
        n = 0
        while current[-1] != 'Z':
            current = nodes[current][rl[n % len(rl)] == 'R']
            n += 1
        return n
    
    print(lcm(*(aaa(c) for c in currents)))

if __name__ == '__main__':
    main()
