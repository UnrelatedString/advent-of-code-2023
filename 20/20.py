#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

from collections import deque

# so I don't have any more accidentally global internal loop variables...
def main():
    d = defaultdict(lambda: ('b', []))#{'button': ('b','broadcaster')}
    states = {}
    parents = defaultdict(list)
    for line in slorp():
        m, ds = line.split(' -> ')
        ds = ds.split(', ')
        if m == 'broadcaster':
            d[m] = ('b', ds)
            for dd in ds:
                parents[dd].append(m)
        else:
            d[m[1:]] = (m[0], ds)
            if m[0] == '%':
                states[m[1:]] = 0
            elif m[0] == '&':
                states[m[1:]] = defaultdict(lambda: 0)
            else:
                assert False
            for dd in ds:
                parents[dd].append(m[1:])
    
    #print(states)
    cs = [0, 0]

    # low = 0, high = 1
    for _ in range(1000):
        q = deque()
        q.append(('broadcaster', 0, 'button'))
        while q:
            recr, recv, frm = q.popleft()
            # print(f'{frm} -{"hliogwh"[not recv::2]}-> {recr}')
            t, dests = d[recr]
            cs[recv] += 1
            if t == 'b':
                outv = recv
            elif t == '%':
                if recv:
                    continue
                states[recr] ^= 1
                outv = states[recr]
            elif t == '&':
                states[recr][frm] = recv
                outv = not all(states[recr][par] for par in parents[recr])
            for dt in dests[::1]:
                q.append((dt, outv, recr))
    
    print(cs[1] * cs[0])

if __name__ == '__main__':
    main()
