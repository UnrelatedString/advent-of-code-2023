#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    connects = defaultdict(list)
    start = None
    for y, r in enumerate(slorp()):
        for x, c in enumerate(r):
            z = complex(x, y)
            for t in {
                '|': [1j, -1j],
                '-': [1, -1],
                'L': [-1j, 1],
                'J': [-1j, -1],
                '7': [1j, -1],
                'F': [1j, 1],
                '.': [],
                'S': []
            }[c]:
                connects[z + t].append(z)
            if c == 'S':
                start = z
    
    
    def tr(c, t):
        n = 0
        p = start
        while c != t:
            n += 1
            nc, = [x for x in connects[c] if x != p and c in connects[x]]
            p = c
            c = nc
        return n
    
    print(tr(*connects[start]) // 2 + 1)

if __name__ == '__main__':
    main()
