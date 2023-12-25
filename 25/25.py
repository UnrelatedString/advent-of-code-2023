#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    conns = defaultdict(list)
    for line in slorp():
        a, bs = line.split(': ')
        for b in bs.split():
            conns[a].append(b)
            conns[b].append(a)
    

    

    # fuck it we ball
    start = next(iter(conns))
    # unvisited = {(start)}
    # visited = set()
    # upstream = defaultdict(list)
    # while unvisited:
    #     current = unvisited.pop()
    #     for n in conns[current]:
    #         if 

    


if __name__ == '__main__':
    main()
