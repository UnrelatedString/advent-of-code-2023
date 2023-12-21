#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    target = 5000
    plot = set()
    start = None
    for y, line in enumerate(slorp()):
        for x, c in enumerate(line):
            z = complex(x, y)
            if c == 'S':
                start = z
            if c != '#':
                plot.add(z)
    w, h = -~x, -~y
    
    unvisited = {start}
    visited = set()
    dists = {}
    n = 0
    rbl = [set(), set()]
    while unvisited & plot or n <= w:
        nun = set()
        for z in unvisited:
            dists[z] = n
            for o in von_neumann:
                nz = z + o
                mnz = complex(z.real % w, z.imag % h)
                if nz in visited or mnz not in plot:
                    continue
                nun.add(nz)
            visited.add(z)
            rbl[n % 2].add(z)
        unvisited = nun
        n += 1
    assert w == h and  w & 1

    s = 0
    r, rem = divmod(target , w)
    oddcs = sum(n * 4 - 1 for n in range(0, r, 2))
    evencs = sum(n * 4 - 1 for n in range(1, r, 2))
    s += oddcs * len(rbl[0] & plot) + evencs * len(rbl[1] & plot)
    #s += len(rbl) * -~(target // w) ** 2
    e = 0
    for z in dists:
        e += (dists[z] ^ rem) & 1 and dists[z] <= rem
    s += e * -~r * 4
    print(s)
    

if __name__ == '__main__':
    main()
