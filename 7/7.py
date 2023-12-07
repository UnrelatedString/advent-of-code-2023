#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    r = 'AKQJT98765432'.index

    hs = []

    for line in slorp():
        h, b = line.split()
        b = int(b)
        p = [
            len(set(h)) == 1,
            len(set(h)) == 2 and any(h.count(c) == 1 for c in h),
            len(set(h)) == 2,
            any(h.count(c) == 3 for c in h),
            len(set(h)) == 3,
            len(set(h)) == 4,
            True
        ].index(True)
        hs.append([p, tuple(map(r, h)), b])
    
    hs.sort()
    s = 0
    for i, x in enumerate(hs):
        s += -~i * x[2]
    print(s)

if __name__ == '__main__':
    main()
