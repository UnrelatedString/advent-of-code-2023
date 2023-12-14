#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

from collections import defaultdict
from functools import lru_cache

# so I don't have any more accidentally global internal loop variables...
def main():
    walls = set()
    rocks = set()

    lines = slorp()
    w, h = len(lines[0]), len(lines)
    for y, line in enumerate(lines):
        for x, v in enumerate(line):
            z = complex(x, y)
            if v == 'O':
                rocks.add(z)
            if v == '#':
                walls.add(z)
    
    @lru_cache(maxsize = None)
    def slide(rock, dir):
        while rock not in walls and 0 <= rock.real < w and 0 <= rock.imag < h:
            rock += dir
        return zround(rock - dir)
    
    rocks = frozenset(rocks)
    history = []
    sums = []
    dir = -1j
    while (rocks, dir) not in history:
        history.append((rocks, dir))
        ds = defaultdict(lambda: 0)
        for r in rocks:
            ds[slide(r, dir)] += 1
    

        s = 0
        rocks = set()
        for d in ds:
            for o in range(ds[d]):
                rocks.add(d - o * dir)
            s += ds[d] * (h - int(d.imag))
        sums.append(s)
        dir *= -1j
        rocks = frozenset(rocks)
    
    i = history.index((rocks, dir))

    # print(i)

    clen = len(history) - i
    cto = 4000000000 - i
    cs, ac = divmod(cto, clen)

    # s = 0
    # s += sum(sums[:i])
    # s += sum(sums[i:]) * cs
    # s += sum(sums[i:i+ac])

    # print(s, sums)

    print(sums[i + ac - 1])



    

if __name__ == '__main__':
    main()
