#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

import re

# so I don't have any more accidentally global internal loop variables...
def main():
    number = re.compile(r'[0-9]+')
    lines = slorp()
    symbols = set()
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
            if c not in '.0123456789':
                symbols.add(complex(x, y))
        if n:
            numbers.append((n, ns, len(l), y))
    
    s = 0
    for n, ns, ne, y in numbers:
        add = False
        for x in range(ns, ne):
            for o in moore:
                if complex(x, y) + o in symbols:
                    add = True
        s += add * int(n)
    print(s)

if __name__ == '__main__':
    main()
