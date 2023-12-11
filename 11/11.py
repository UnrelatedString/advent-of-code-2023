#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

from functools import lru_cache

# so I don't have any more accidentally global internal loop variables...
def main():
    xs = set()
    ys = set()
    gs = []
    for y, r in enumerate(slorp()):
        for x, c in enumerate(r):
            z = (x, y)
            
            if c == '#':
                xs.add(x)
                ys.add(y)
                gs.append(z)
    
    # print(len(xs), len(ys))

    def od(within):
        @lru_cache
        def d(a, b):
            if b < a:
                return d(b, a)
            s = 0
            for n in range(int(a), int(b)):
                s += 1
                s += n not in within
            return s
        return d
    
    xd, yd = od(xs), od(ys)

    s = 0
    for i, a in enumerate(gs):
        for b in gs[:i]:
            s += xd(a[0], b[0])
            s += yd(a[1], b[1])
            # print(s, a, b)
    print(s)

if __name__ == '__main__':
    main()
