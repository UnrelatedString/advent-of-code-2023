#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    ts = list(map(int, input().split()[1:]))
    ds = list(map(int, input().split()[1:]))

    prod = 1

    for t, d in zip(ts, ds):
        # x * (t - x) > d basically
        # wait i can just brute force this
        s = 0
        for x in range(t):
            s += x * (t - x) > d
        prod *= s
    
    print(prod)

if __name__ == '__main__':
    main()
