#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():

    def co(rs):
        s = 0
        for i in range(0, len(rs)):
            pf = rs[:i][::-1]
            sf = rs[i:]
            ss = 0
            for a, b in zip(pf, sf):
                for A, B in zip(a, b):
                    ss += A != B
            s += i * (ss == 1)
        return s

    s = 0
    for g in line_groups(slorp()):
        a = 0
        a += 100 * co(g)
        a += co(list(zip(*g)))
        assert a
        s += a
    print(s)

if __name__ == '__main__':
    main()
