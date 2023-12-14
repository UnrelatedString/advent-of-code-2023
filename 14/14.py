#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

from collections import defaultdict

# so I don't have any more accidentally global internal loop variables...
def main():
    walls = defaultdict(lambda: -1)
    s = 0
    lines = slorp()
    for y, line in enumerate(lines):
        for x, v in enumerate(line):
            if v == 'O':
                walls[x] += 1
                s += len(lines) - walls[x]
            if v == '#':
                walls[x] = y
    print(s)

if __name__ == '__main__':
    main()
