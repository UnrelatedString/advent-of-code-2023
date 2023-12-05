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
            snew = [[l] for l in s]
            for i, (a, b) in enumerate(s):
                if f <= a < b <= f + l:
                    new[i] += [
                        (a - f + d, b - f + d),
                    ]
                    snew[i] = [(a, a)]
                elif f <= a < f + l:
                    new[i] += [
                        (a - f + d, d + l),
                        # (f + l, b),
                    ]
                    snew[i] = [(f + l, b)]
                elif f < b <= f + l:
                    new[i] += [
                        (d, b - f + d),
                        # (a, f),
                    ]
                    snew[i] = [(a, f)]
                elif a <= f < f + l <= b:
                    new[i] += [
                        #(a, f),
                        (d, d + l),
                        #(d + l, b)
                    ]
                    snew[i] = [
                        (a, f),
                        #(d, d + l),
                        (d + l, b)
                    ]
            s = [t for l in zip(*snew) for t in l]
            new += [[] for _ in range(len(new), len(s))]
            # print(new)
        s += [t for l in new for t in l]
        s = [(a, b) for a, b in s if a < b]

        # print(s)

    print(min(min(s)))
        
        #print(s)

if __name__ == '__main__':
    main()
