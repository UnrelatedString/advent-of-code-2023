#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    s = 0
    for l in slorp():
        n, m = l.split(': ')
        w, y = m.split(' | ')
        p = len(set(w.split()) & set(y.split()))
        if p:
            s += 2 ** ~-p
    print(s)

if __name__ == '__main__':
    main()
