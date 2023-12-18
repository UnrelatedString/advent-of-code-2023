#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    edge = set((0,))
    left = set()
    right = set()
    z = 0
    for line in slorp():
        d, n, _c = line.split()
        d = 1j ** 'RDLU'.index(d)
        # print(d, line)
        n = int(n)
        for _ in range(n):
            left.add(z + 1j * d)
            right.add(z - 1j * d)
            z += d
            left.add(z + 1j * d)
            right.add(z - 1j * d)
            edge.add(z)
    
    w, h = -~int(max(z.real for z in edge)), -~int(max(z.imag for z in edge))
    zw, zh = ~-int(min(z.real for z in edge)), ~-int(min(z.imag for z in edge))
    
    def flood(unvisited):
        visited = set()
        while unvisited:
            current = unvisited.pop()
            visited.add(current)
            for o in von_neumann:
                z = current + o
                if z in edge or z in visited:
                    continue
                if not (zw <= z.real < w and zh <= z.imag < h):
                    return 0
                unvisited.add(z)
        return len(visited)

    print(flood(left - edge) + flood(right - edge) + len(edge))
    # print(edge)



if __name__ == '__main__':
    main()
