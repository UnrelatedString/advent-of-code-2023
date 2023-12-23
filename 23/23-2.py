#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())
# from sys import setrecursionlimit
# setrecursionlimit(9999)

# so I don't have any more accidentally global internal loop variables...
def main():
    path = set()
    for y, line in enumerate(slorp()):
        for x, c in enumerate(line):
            z = complex(x, y)
            if c != '#':
                path.add(z)
    w, h = -~x, -~y
    
    start = 1
    finish = complex(w - 2, h - 1)
    assert finish in path

    crossroads = set()

    for y in range(h):
        for x in range(w):
            z = complex(x, y)
            n = 0
            for o in von_neumann:
                n += z + o in path
            if n > 2:
                crossroads.add(z)
    
    ds = defaultdict(lambda: 0)

    m = 0

    # print(len(crossroads))

    heads = deque()
    heads.append((start, None, 0, frozenset()))
    while heads:
        at, prev, d, hist = heads.pop()
        if at in crossroads:
            hist |= {at}
            if ds[(at, hist)] > d:
                continue
            ds[(at, hist)] = d
        if at == finish:
            m = max(m, d)
            print(d, m, len(heads))
            continue
        for o in von_neumann:
            z = at + o
            if z in path and z not in hist and \
                z != prev and \
                0 <= z.real < w and \
                0 <= z.imag < h:
                heads.append((z, at, d + 1, hist))
    
    print(m)
        
        

if __name__ == '__main__':
    main()
