#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    connects = defaultdict(list)
    start = None
    for y, r in enumerate(slorp()):
        for x, c in enumerate(r):
            z = complex(x, y)
            for t in {
                '|': [1j, -1j],
                '-': [1, -1],
                'L': [-1j, 1],
                'J': [-1j, -1],
                '7': [1j, -1],
                'F': [1j, 1],
                '.': [],
                'S': []
            }[c]:
                connects[z + t].append(z)
            if c == 'S':
                start = z
    
    w, h = -~x, -~y

    loop = {start, *connects[start]}

    def tr(c, t):
        n = 0
        
        p = start
        loop.add((c + p) / 2)
        loop.add((t + p) / 2)

        while c != t:
            n += 1
            nc, = [x for x in connects[c] if x != p and c in connects[x]]
            p = c
            c = nc
            
            loop.add(c)
            loop.add((c + p) / 2)

        return n
    
    tr(*connects[start])

    unvisited = {-1-1j} # pray
    
    visited = set()
    while unvisited:
        c = unvisited.pop()
        visited.add(c)
        for o in von_neumann:
            z = c + o / 2
            if z not in visited and z not in loop and -1 <= z.real <= w and -1 <= z.imag <= h:
                unvisited.add(z)
    
    print(-~-~w * -~-~h - sum(z == zround(z) for z in (loop | visited)))


if __name__ == '__main__':
    main()
