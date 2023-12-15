#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    def hh(cc):
        s = 0
        for c in cc:
            s += ord(c)
            s *= 17
            s %= 256
        return s
    s = 0
    bs = defaultdict(lambda: ([], []))
    for h in ''.join(slorp()).split(','):

        # l, o = h[:2], h[2]
        # b = hh(l)
        if h[-2] == '=':
            l = h[:-2]
            b = hh(l)
            n = h[-1]
            if l in bs[b][0]:
                bs[b][1][bs[b][0].index(l)] = n
            else:
                bs[b][0].append(l)
                bs[b][1].append(n)
        elif h[-1] == '-':
            l = h[:-1]
            b = hh(l)
            if l in bs[b][0]:
                i = bs[b][0].index(l)
                bs[b][0][i:i+1] = []
                bs[b][1][i:i+1] = []
        else:
            print(h)#assert False

    for b in bs:
        for i, n in enumerate(bs[b][1]):
            s += -~b * -~i * int(n)
    print(s)

if __name__ == '__main__':
    main()
