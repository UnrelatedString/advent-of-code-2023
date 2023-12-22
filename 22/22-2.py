#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    cubes = []
    for line in slorp():
        a, b = line.split('~')
        cubes.append(sorted((tuple(map(int,a.split(','))), tuple(map(int,b.split(','))))))

    # or really, Z...
    def decy(t):
        return tuple_augment(t, 2, lambda n: n - 1)
    def incy(t):
        return tuple_augment(t, 2, lambda n: n + 1)


    space = {}
    def over_brick(brick, f):
        a, b = brick
        for x in range(a[0], -~b[0]):
            for y in range(a[1], -~b[1]):
                for z in range(a[2], -~b[2]):
                    yield f((x, y ,z))
    
    def add_brick(brick):
        any(over_brick(brick, lambda the: space.__setitem__(the, brick)))

    cubes.sort(key = lambda t: min(t[0][2], t[1][2]))
    fallen = []
    rrr = {}
    for a, b in cubes:
        bottom = min(a[2], b[2])
        for o in range(0, bottom):
            a = decy(a)
            b = decy(b)
            rests_on = set()
            # for A, B in fallen:
            #     if all(a[i] <= A[i] == B[i] <= b[i] or A[i] <= a[i] == b[i] <= B[i] for i in range(3)):
            #         rests_on.append((A, B))
            for other in over_brick((a, b), lambda c: space.get(c,  None)):
                if other:
                    rests_on.add(other)
            if rests_on:
                a, b = incy(a), incy(b)
                rrr[(a, b)] = rests_on
                fallen.append((a, b))
                break
        else:
            rrr[(a, b)] = set()
            fallen.append((a, b))
        add_brick((a, b))
    
    fallen.sort(key = lambda t: min(t[0][2], t[1][2]))
    # @lru_cache(maxsize=None)
    # def totr(brick, without):
    #     s = 1
    #     without |= {brick}
    #     new = set()
    #     for r in fallen:
    #         if r == brick: continue
    #         if r in rrr[r] and without >= rrr[r]:
    #             new.add(r)
    #     without |= new
    #     for r in new:
    #         s += totr(r, without)
    #     return s
    # print(sum(~-totr(brick, frozenset()) for brick in fallen))
    s = 0
    for rem in fallen:
        without = {rem}
        for r in fallen:
            if r in without: continue
            if rrr[r] <= without and rrr[r]:
                without.add(r)
                s += 1
    print(s)



if __name__ == '__main__':
    main()
