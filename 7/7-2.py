#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    r = 'AKQT98765432J'.index

    hs = []
    bets = {}

    for i, line in enumerate(slorp()):
        h, b = line.split()
        b = int(b)
        j = set(h) - {'J'}

        # five of a kind
        if len(j) <= 1:
            p = 0
        # four of a kind
        elif len(j) == 2 and any(h.count(c) == 1 for c in j):
            p = 1
        # full house
        elif len(j) == 2:
            p = 2
        # three of a kind
        elif any(h.count(c) == 3 for c in h) or (
            any(h.count(c) == 2 for c in h) and 'J' in h
        ):
            assert len(j) == 3
            p = 3
        # two pair
        elif any(c != d and h.count(c) == 2 and h.count(d) == 2 for c in h for d in h):
            assert len(j) == 3
            p = 4
        # one pair
        elif len(j) == 4:
            p = 5
        # high card
        else:
            assert len(j) == 5
            p = 6
        
        hs.append([-p, *(-r(c) for c in h), h, i])
        bets[i] = b
    
    # hs = hs[::-1]
    hs = sorted(hs, key = lambda l: l[:-2])
    # print(*hs)
    s = 0
    for i, x in enumerate(hs[::-1]):
        # print(i, x[-2])
        s += (len(hs) - i) * bets[x[-1]]
    print(s)

if __name__ == '__main__':
    main()
