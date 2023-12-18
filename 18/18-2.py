#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    corners = [0]
    z = 0
    es = 0
    for line in slorp():
        _d, _n, c = line.split()
        c = c[2:]
        d = 1j ** '0123'.index(c[5])
        n = int(c[:5], base = 16)
        z += d * n
        corners.append(z)
        es += n
    
    # w, h = -~int(max(z.real for z in edge)), -~int(max(z.imag for z in edge))
    # zw, zh = ~-int(min(z.real for z in edge)), ~-int(min(z.imag for z in edge))
    
    # def flood(unvisited):
    #     visited = set()
    #     while unvisited:
    #         current = unvisited.pop()
    #         visited.add(current)
    #         for o in von_neumann:
    #             z = current + o
    #             if z in edge or z in visited:
    #                 continue
    #             if not (zw <= z.real < w and zh <= z.imag < h):
    #                 return 0
    #             unvisited.add(z)
    #     return len(visited)

    # print(flood(left - edge) + flood(right - edge) + len(edge))
    # # print(edge)


    # s = 0
    # for y in range(zh, h):
    #     i = False
    #     for x in range(zw, w):
    #         z = complex(x, y)
    
    # print(es)
    s = 0
    for i in range(len(corners)-1):
        s += int(corners[i].imag * (corners[i-1%len(corners)].real - corners[i+1].real))
    print((s + es) // 2 + 1)
    #  1904809882966
    #  952408144115


if __name__ == '__main__':
    main()
