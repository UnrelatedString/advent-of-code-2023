#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

def e(l):
    ds = [b - a for a, b in zip(l, l[1:])]
    if any(ds):
        # print(ds, e(ds) + ds[-1])
        return ds[0] - e(ds)
    else:
        return 0


# so I don't have any more accidentally global internal loop variables...
def main():
    s = 0
    for h in slorp():
        h = list(map(int, h.split()))
        s += - e(h) + h[0]
    print(s)

if __name__ == '__main__':
    main()
