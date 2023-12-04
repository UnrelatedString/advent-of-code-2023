#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    c = defaultdict(lambda: 1)
    for l in slorp():
        n, m = l.split(': ')
        n = int(n[5:])
        c[n]
        w, y = m.split(' | ')
        i = set(w.split()) & set(y.split())
        for j in range(len(i)):
            c[int(n-~j)] += c[n]
    print(sum(c.values()))

if __name__ == '__main__':
    main()
