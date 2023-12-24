#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    lb, ub = 200000000000000, 400000000000000
    stones = []
    for line in slorp():
        (x, y, z), (dx, dy, dz) = (map(int, g.split(', ')) for g in line.split(' @ '))
        stones.append(((x, y, z), (dx, dy, dz)))
    s = 0
    for i, a in enumerate(stones):
        (ax, ay, az), (adx, ady, adz) = a
        asl = ady/adx
        ain = ay - (asl * ax)
        for b in stones[:i]:
            # print(a, b)
            (bx, by, bz), (bdx, bdy, bdz) = b
            bsl = bdy/bdx
            if asl != bsl:
                bin = by - (bsl * bx)
                intx = (bin-ain)/(asl-bsl)
                inty = asl * intx + ain
                if not (lb <= intx <= ub):
                    continue
                if not (lb <= inty <= ub):
                    continue
                if (intx >= ax) != (adx >= 0):
                    continue
                if (intx >= bx) != (bdx >= 0):
                    continue
                if (inty >= ay) != (ady >= 0):
                    continue
                if (inty >= by) != (bdy >= 0):
                    continue
                s += 1
            else:
                # hope none ever share paths
                pass
    print(s)



if __name__ == '__main__':
    main()
