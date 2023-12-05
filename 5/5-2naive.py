#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    s, *gs = line_groups(slorp())

    il = lambda l: list(map(int, l.split()))

    s = il(s[0].split(': ')[1])
    s = [x for a, b in zip(s[::2],s[1::2]) for x in range(a, a + b)]

    for g in gs:
        new = s[:]
        for m in g[1:]:
            d, f, l = il(m)
            for i, S in enumerate(s):
                if f <= S < f + l:
                    new[i] = d + S - f
                    #print(d, f, l, S, new[i])
        s = new
        #print(s)
    
    print(min(s))

if __name__ == '__main__':
    main()
