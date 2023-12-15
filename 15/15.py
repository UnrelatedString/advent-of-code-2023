#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    def hh(cc):
        s = 0
        for c in cc:
            s += ord(c)
            s *= 17
            s %= 256
        return s
    s = 0
    for h in ''.join(slorp()).split(','):
        s += hh(h)
    print(s)

if __name__ == '__main__':
    main()
