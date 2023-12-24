#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    stones = []
    # third = set()
    for line in slorp():
        (x, y, z), (dx, dy, dz) = (map(int, g.split(', ')) for g in line.split(' @ '))
        stones.append(((x, y, z), (dx, dy, dz)))
        # third.add(((x + dx * 3, y + dy * 3, z + dz * 3)))
    


    # for i, a in enumerate(stones):
    #     (ax, ay, az), (adx, ady, adz) = a
    #     for b in stones[:i]:
    #         # print(a, b)
    #         (bx, by, bz), (bdx, bdy, bdz) = b
    #         ax += adx
    #         ay += ady
    #         az += adz
    #         bx += bdx * 2
    #         by += bdy * 2
    #         bz += bdz * 2
    #         rdx, rdy, rdz = (bx - ax), (by - ay), (bz - az)
    #         if (bx + rdx, by + rdy, bz + rdz) in third:
    #             print('asdfda')


    # for i, a in enumerate(stones):
    #     (ax, ay, az), (adx, ady, adz) = a
    #     asl = ady/adx
    #     ain = ay - (asl * ax)
    #     for b in stones[:i]:
    #         # print(a, b)
    #         (bx, by, bz), (bdx, bdy, bdz) = b
    #         bsl = bdy/bdx
    #         if asl != bsl:
    #             bin = by - (bsl * bx)
    #             intx = (bin-ain)/(asl-bsl)
    #             inty = asl * intx + ain
    #             taa = (ax - intx) / adx
    #             tbb = (bx - intx) / bdx
                
    #             if (intx >= ax) != (adx >= 0):
    #                 continue
    #             if (intx >= bx) != (bdx >= 0):
    #                 continue
    #             if (inty >= ay) != (ady >= 0):
    #                 continue
    #             if (inty >= by) != (bdy >= 0):
    #                 continue
    #             if -1 < (az + adz * taa) - (bz + bdz * tbb) < 1:
    #                 print('yay')
    #         else:
    #             # none are ever parallel in 3d
    #             pass

    a, b, *rest = stones
    (ax, ay, az), (adx, ady, adz) = a
    (bx, by, bz), (bdx, bdy, bdz) = b
    st = 1
    while True:        
        for ta in range(st):
            tb = st - ta
            if ta == tb:
                continue
            dt = tb - ta
            rdx, rdy, rdz = (bx + bdx * tb - ax - adx * ta) / dt, (by + bdy * tb - ay - ady * ta) / dt, (bz + bdz * tb - az - adz * ta) / dt
            if rdx == 0 or rdy == 0:
                continue
            if not (rdx % 1 == rdy % 1 == rdz % 1 == 0):
                continue
            rx, ry, rz = ax + adx * ta, ay + ady * ta, az + adz * ta
            rsl = rdy/rdx
            rin = ry - (rsl * rx)
            ints = [(a, ax + adx * ta, ay + ady * ta, az + adz * ta), (b, bx + bdx * tb, by + bdy * tb, bz + bdz * tb)]
            for c in rest:
                (cx, cy, cz), (cdx, cdy, cdz) = c
                # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                
                
                csl = cdy/cdx
                cin = cy - (csl * cx)

                intx = (cin-rin)/(rsl-csl)
                inty = rsl * intx + rin
                # print(inty, csl * intx + cin)
                trr = (intx - rx) / rdx
                tcc = (intx - cx) / cdx
                rintz = rz + rdz * trr
                cintz = cz + cdz * tcc
                if -1 < rintz - cintz < 1:
                    ints.append((c, intx, inty, rz + rdz * trr))
                    continue
                else:
                    # print(c, ta, tb, rdx, rdy, rdz, intx, inty, rintz, cintz, trr, tcc)
                    break
            else:
                ints.sort(key = lambda eeeee: eeeee[1:])
                print('yippee')
                exit()
        st += 1

            


if __name__ == '__main__':
    main()
