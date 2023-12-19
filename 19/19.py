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
    
    s = 0
    pt = namedtuple('part', list('xmas'))
    for l in pls:
        p = eval(f'pt({l[1:-1]})')
        fl = 'in'
        while fl not in 'AR':
            for *cond, res in fls[fl]:
                if not cond:
                    fl = res
                    break
                cond, = cond
                if eval('p.'+cond.replace('=','==')):
                    fl = res
                    break
        if fl == 'A':
            s += sum(p)
    print(s)
    


if __name__ == '__main__':
    main()
