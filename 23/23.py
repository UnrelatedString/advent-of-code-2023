#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())
# from sys import setrecursionlimit
# setrecursionlimit(9999)

# so I don't have any more accidentally global internal loop variables...
def main():
    path = {}
    for y, line in enumerate(slorp()):
        for x, c in enumerate(line):
            z = complex(x, y)
            if c == '.':
                path[z] = 0
            elif c != '#':
                path[z] = 1j ** '>v<^'.index(c)
    w, h = -~x, -~y
    
    start = 1
    finish = complex(w - 2, h - 1)
    assert path[finish] == 0

    @lru_cache(maxsize=None)
    def dp(at, history = frozenset()):
        tr = 0
        lr = 0
        while True:
            # print(at, path[at])
            if at == finish:
                return max(tr, lr)
            choices = []
            for o in von_neumann:
                z = at + o
                if z in path and z not in history and \
                    (o == path[at] or path[at] == 0) and \
                    0 <= z.real < w and \
                    0 <= z.imag < h:
                    # print(z)
                    choices.append((z, history | {at}))
            if not choices:
                return tr
            (at, history), *rest = choices
            for c in rest:
                n = dp(*c)
                if n:
                    tr = max(tr, n + 1 + lr)
            lr += 1
                
    
    print(dp(start))
    # print(dp(finish - 1j))
    # print(path[finish - 1j])


if __name__ == '__main__':
    main()
