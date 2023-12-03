#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

import re

# so I don't have any more accidentally global internal loop variables...
def main():
    number = re.compile(r'[0-9]+')
    lines = slorp()
    gears = set()
    numbers = []
    for y, l in enumerate(lines):
        n, ns = '', None
        for x, c in enumerate(l):
            if c in '0123456789':
                n += c
                ns = ns or x
            elif n:
                numbers.append((n, ns, x, y))
                n = ''
                ns = None
            if c == '*':
                gears.add(complex(x, y))
        if n:
            numbers.append((n, ns, len(l), y))
    
    gearss = defaultdict(list)

    s = 0
    for n, ns, ne, y in numbers:
        adjs = set()
        for x in range(ns, ne):
            z = complex(x,y)
            for o in moore:
                if z + o in gears:
                    adjs.add(z + o)
     #   print(adjs)
        for a in adjs:
            gearss[a].append(int(n))
    #print(gearss, gears, numbers)
    for a, p in gearss.items():
        if len(p) == 2:
            x, y = p
            s += x * y

    print(s)

if __name__ == '__main__':
    main()
