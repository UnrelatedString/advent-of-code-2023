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
    
    s = 0
    for cube in fallen:
        safe = True
        for other in fallen:
            if cube in rrr[other]:
                if len(rrr[other]) == 1:
                    safe = False
                    
                    break
        s += safe
    print(s)
    # print(rrr)
    # print(space)



if __name__ == '__main__':
    main()
