#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    grid = slorp()
    w, h=  len(grid[0]), len(grid)
    m = 0
    for r, o, d in [
        [range(w), 0, 1j],
        [range(w), 1j*h, -1j],
        [range(h), 0, 1],
        [range(h), w, -1]
    ]:
        p = 1j ** (d.imag == 0)
        for AAA in r:
            m = max(m,
                    lmao(grid, (o + (AAA * p), d)))
    print(m)
        

def lmao(grid, init):
    
    beams = {init}
    history = set()
    rhistory = set()
    while beams:
        nb = set()
        for b, d in beams:
            if not (0 <= b.real < len(grid[0]) and 0 <= b.imag < len(grid)):
                continue
            if (b, d) in rhistory:
                continue
            history.add(b)
            rhistory.add( (b, d))
            c = zind(b, grid)
            # print(c)
            if c == '|' and d.imag == 0:
                d *= 1j
                nb |= {(b - d, -d), (b + d, d)}
            elif c == '-' and d.real == 0:
                d *= 1j
                nb |= {(b - d, -d), (b + d, d)}
            elif c == '\\' and d in {-1j, -1}:
                d = ({-1j, -1} - {d}).pop()
                nb |= {(b + d, d)}
            elif c == '\\' and d in {1j, 1}:
                d = ({1j, 1} - {d}).pop()
                nb |= {(b + d, d)}
            elif c == '/' and d in {-1j, 1}:
                d = ({-1j, 1} - {d}).pop()
                nb |= {(b + d, d)}
            elif c == '/' and d in {1j, -1}:
                d = ({1j, -1} - {d}).pop()
                nb |= {(b + d, d)}
            else:
                nb |= {(b + d, d)}
        beams = nb
        # print(beams)
    return(len(history))


if __name__ == '__main__':
    main()
