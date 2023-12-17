#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

import heapq

# so I don't have any more accidentally global internal loop variables...
def main():
    losses = [[int(n) for n in r] for r in slorp()]
    w, h = len(losses[0]), len(losses)
    dest = complex(~-w, ~-h)
    dests = {(dest, s, d) for s in range(3, 11) for d in von_neumann}

    start = 0, 0, 0
    unvisited = []
    heapq.heappush(unvisited, (0, repr(start)))
    visited = set()
    ds = defaultdict(lambda: float('inf'))
    ds[start] = 0

    while not visited & dests:
        _, current = heapq.heappop(unvisited)
        current = eval(current)
        
        visited.add(current)
        for o in von_neumann:
            cp, cs, cd = current
            z = cp + o
            s = -~cs if o == cd else 0
            if not (0 <= z.real < w and 0 <= z.imag < h):
                continue
            if s >= 10:
                continue
            if o == -cd:
                continue
            if cd and o != cd and cs <= 2:
                continue
            if (z, s, o) in visited:
                continue
            ds[z, s, o] = min(ds[z, s, o], ds[current] + zind(z, losses))
            heapq.heappush(unvisited, (ds[z, s, o], repr(z, s, o)))
        # print(unvisited)
    # print(ds)
    print(min((ds[d]) for d in dests))
    


if __name__ == '__main__':
    main()
