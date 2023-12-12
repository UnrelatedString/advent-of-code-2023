#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

from itertools import groupby
from functools import lru_cache

# so I don't have any more accidentally global internal loop variables...
def main():
    s = 0
    for line in slorp():
        ss, gs = line.split(' ')
        gs = tuple(map(int, gs.split(',')))
        @lru_cache
        def dp(i, within, gg):
            if (within and not gg) or (gg and gg[0] < within):
                return 0
            if i == len(ss):
                return gg == () or gg == (within,)
            c = ss[i]
            r = 0
            if c != '#':
                if within == 0:
                    r += dp(i + 1, 0, gg)
                elif gg and within == gg[0]:
                    r += dp(i + 1, 0, gg[1:])
            if c != '.':
                r += dp(i + 1, within + 1, gg)
            return r
        s += dp(0, 0, gs)
    print(s)
            


if __name__ == '__main__':
    main()
