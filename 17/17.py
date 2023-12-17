#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    losses = [[int(n) for n in r] for r in slorp()]
    w, h = len(losses[0]), len(losses)
    dest = complex(~-w, ~-h)
    dests = {(dest, s, d) for s in range(4) for d in von_neumann}

    start = 0, 0, 0
    unvisited = {start}
    visited = set()
    ds = defaultdict(lambda: float('inf'))
    ds[start] = 0

    while not visited & dests:
        current = min(unvisited, key = lambda n: ds[n])
        unvisited.remove(current)
        visited.add(current)
        for o in von_neumann:
            cp, cs, cd = current
            z = cp + o
            s = -~cs if o == cd else 0
            if not (0 <= z.real < w and 0 <= z.imag < h):
                continue
            if s >= 3:
                continue
            if o == -cd:
                continue
            if (z, s, o) in visited:
                continue
            ds[z, s, o] = min(ds[z, s, o], ds[current] + zind(z, losses))
            unvisited.add((z, s, o))
        # print(unvisited)
    # print(ds)
    print(min((ds[d]) for d in dests))
    


if __name__ == '__main__':
    main()
