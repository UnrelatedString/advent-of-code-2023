#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    target = 64
    plot = set()
    start = None
    for y, line in enumerate(slorp()):
        for x, c in enumerate(line):
            z = complex(x, y)
            if c == 'S':
                start = z
            if c != '#':
                plot.add(z)
    
    unvisited = {start}
    visited = set()
    rbl = set()
    for n in range(target+1):
        nun = set()
        for z in unvisited:
            for o in von_neumann:
                nz = z + o
                if nz in visited or nz not in plot:
                    continue
                nun.add(nz)
            visited.add(z)
            if not n % 2:
                rbl.add(z)
        unvisited = nun
    print(len(rbl))


if __name__ == '__main__':
    main()
