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

    # # low = 0, high = 1
    # n = 1
    # # core = {'broadcaster': (0, 'button')}
    # # reached_at = {}
    
    # while True:
    #     n <<= 1
    #     # reached = {**core}
    #     q = deque()
    #     q.append(('broadcaster', 0, 'button'))
    #     while q:
    #         recr, recv, frm = q.popleft()
    #         # reached[recr] = recv, frm
    #         if recr == 'rx' and not recv:
    #             print(n)
    #             return
    #         # print(f'{frm} -{"hliogwh"[not recv::2]}-> {recr}')
    #         t, dests = d[recr]
    #         #cs[recv] += 1
    #         if t == 'b':
    #             outv = recv
    #         elif t == '%':
    #             if recv:
    #                 continue
    #             states[recr] |= 1
    #             outv = states[recr]
    #             # if recr not in reached_at:
    #             #     reached_at[recr] = n
    #             #     print(n, recr, parents[recr])
    #         elif t == '&':
    #             states[recr][frm] = recv
    #             outv = not all(states[recr][par] for par in parents[recr])
    #         for dt in dests[::1]:
    #             q.append((dt, outv, recr))
    
    # def cdlcdsalkcjv(root, cyc = ()):
    #     if root == 'broadcaster':
    #         return 0
    #     f = d[root][0] == '%'
    #     return f + min(cdlcdsalkcjv(par, cyc + (root,)) for par in parents[root] + ['rx'] if par not in cyc)
    # print(*(cdlcdsalkcjv(aaaaa) for aaaaa in 'kb kx jl cz fx bf lr bl bs pp qv xm'.split()))
    

    pattern = deque()
    pattern.append(('broadcaster', 0, 'button'))
    n = 0
    while pattern:
        q, pattern = pattern, deque() # q = pattern.copy()
        n += 1
        while q:
            recr, recv, frm = q.popleft()
            # print(f'{frm} -{"hliogwh"[not recv::2]}-> {recr}')
            if recr == 'rx' and not recv:
                print(1 << n)
                return
            t, dests = d[recr]
            if t == 'b':
                outv = recv
            elif t == '%':
                if recv:
                    continue
                states[recr] ^= 1
                outv = states[recr]
                if outv:
                    pattern.append((recr, recv, frm))
            elif t == '&':
                states[recr][frm] = recv
                outv = not all(states[recr][par] for par in parents[recr])
            for dt in dests[::1]:
                q.append((dt, outv, recr))
                # if t == '%' and d[dt][0] == '%' and outv:
                #     pattern.append((dt, 0, recr))
        print(n, pattern, parents['rx'])
    
    assert False
    

if __name__ == '__main__':
    main()
