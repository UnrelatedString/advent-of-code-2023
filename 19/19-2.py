#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

from collections import namedtuple
# so I don't have any more accidentally global internal loop variables...
def main():
    fls = {}
    flsls, pls = line_groups(slorp())
    for l in flsls:
        name, r = l.split('{')
        r = r[:-1]
        fls[name] = [step.split(':') for step in r.split(',')]
    
    
    pt = namedtuple('part', list('xmas'))
    def narrow(fl, mins, maxes):
        if fl == 'R':
            return 0
        if fl == 'A':
            return -~(maxes.x - mins.x) * -~(maxes.m - mins.m) * -~(maxes.a - mins.a) * -~(maxes.s - mins.s)
        s = 0
        for *cond, res in fls[fl]:
            if not cond:
                s += narrow(res, mins, maxes)
            else:
                cond, = cond
                op = cond[1]
                var = cond[0]
                val = int(cond[2:])
                if op == '=':
                    # cheat on this one lol
                    s += narrow(res,
                                mins._replace(**{var: val}),
                                maxes._replace(**{var: val}))
                    s += narrow(res,
                                mins._replace(**{var: val + 1}),
                                maxes)
                    maxes = maxes._replace(**{var: val - 1})
                elif op == '<':
                    s += narrow(res,
                                mins,
                                maxes._replace(**{var: val - 1}))
                    mins = mins._replace(**{var: val})
                elif op == '>':
                    # cheat on this one lol
                    s += narrow(res,
                                mins._replace(**{var: val + 1}),
                                maxes)
                    maxes = maxes._replace(**{var: val})
                else:
                    assert False
        return s
    
    print(narrow('in',
                 pt(1, 1, 1, 1),
                 pt(4000, 4000, 4000, 4000)))
                    


if __name__ == '__main__':
    main()
