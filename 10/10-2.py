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
    
    w, h = -~x, -~y

    loop = {start, *connects[start]}
    left, right = set(), set()

    def tr(c, t):
        n = 0
        
        p = start

        dir = c - p
        left.add(c + (dir * 1j))
        right.add(c - (dir * 1j))

        while c != t:
            n += 1
            nc, = [x for x in connects[c] if x != p and c in connects[x]]
            p = c
            c = nc
            
            loop.add(c)
            dir = c - p
            left.add(c + (dir * 1j))
            right.add(c - (dir * 1j))
            left.add(p + (dir * 1j))
            right.add(p - (dir * 1j))
        dir = c - p
        left.add(c + (dir * 1j))
        right.add(c - (dir * 1j))
        return n
    
    tr(*connects[start])

    # print(left, right)

    # unvisited = {-1-1j} # pray
    
    def flood(f):
        unvisited = f
        visited = set()
        while unvisited:
            c = unvisited.pop()
            visited.add(c)
            for o in von_neumann:
                z = c + o
                if z not in visited and z not in loop and -1 <= z.real <= w and -1 <= z.imag <= h:
                    unvisited.add(z)
        if -1-1j in visited:
            return 0
        return len(visited)
    
    # print(-~-~w * -~-~h - len(visited) - len(loop))

    # print({complex(x, y) for x in range(w) for y in range(h)} - flood(left) - flood(right) - loop)

    assert not (left & right) - loop

    print(max(flood(left - loop), flood(right - loop)))

if __name__ == '__main__':
    main()
