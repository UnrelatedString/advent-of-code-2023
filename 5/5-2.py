#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

# so I don't have any more accidentally global internal loop variables...
def main():
    s, *gs = line_groups(slorp())

    il = lambda l: list(map(int, l.split()))

    s = il(s[0].split(': ')[1])
    s = [(a, a + b) for a, b in zip(s[::2],s[1::2])]

    for g in gs:
        #print(s)
        new = [[] for _ in s]
        for m in g[1:]:
            d, f, l = il(m)
            for i, (a, b) in enumerate(s):
                if f <= a < b <= f + l:
                    new[i] += [
                        (a - f + d, b - f + d),
                    ]
                    s[i] = (0, 0)
                elif f <= a < f + l:
                    new[i] += [
                        (a - f + d, d + l),
                    ]
                    s[i] = (f + l, b)
                elif f <= b <= f + l:
                    new[i] += [
                        (d, b - f + d),
                    ]
                    s[i] = (a, f)
            #print(new)
        s = [(a, b) for l, o in zip(new, s) for a, b in (l + [o]) if a < b]

        #print(s)

    print(min(min(s)))
        
        #print(s)

if __name__ == '__main__':
    main()
