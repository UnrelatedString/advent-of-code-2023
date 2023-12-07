#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    r = 'AKQJT98765432'.index

    hs = []
    bets = {}

    for i, line in enumerate(slorp()):
        h, b = line.split()
        b = int(b)
        
        # five of a kind
        if any(h.count(c) == 5 for c in h):
            assert len(set(h)) == 1
            p = 0
        # four of a kind
        elif any(h.count(c) == 4 for c in h) and any(h.count(c) == 1 for c in h):
            assert len(set(h)) == 2
            p = 1
        # full house
        elif any(h.count(c) == 3 for c in h) and any(h.count(c) == 2 for c in h):
            assert len(set(h)) == 2
            p = 2
        # three of a kind
        elif any(h.count(c) == 3 for c in h):
            assert len(set(h)) == 3
            p = 3
        # two pair
        elif any(c != d and h.count(c) == 2 and h.count(d) == 2 for c in h for d in h):
            assert len(set(h)) == 3
            p = 4
        # one pair
        elif any(h.count(c) == 2 for c in h):
            assert len(set(h)) == 4
            p = 5
        # high card
        else:
            assert len(set(h)) == 5
            p = 6
        
        hs.append([-p, *(-r(c) for c in h), h, i])
        bets[i] = b
    
    # hs = hs[::-1]
    hs = sorted(hs, key = lambda l: l[:-2])
    # print(*hs)
    s = 0
    for i, x in enumerate(hs[::-1]):
        print(i, x[-2])
        s += (len(hs) - i) * bets[x[-1]]
    print(s)

if __name__ == '__main__':
    main()
