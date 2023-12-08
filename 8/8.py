#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    rl = input()
    input()
    nodes = {}
    for line in slorp():
        f, lr = line.split(' = ')
        nodes[f] = lr[1:-1].split(', ')
    
    n = 0
    current = 'AAA'
    while current != 'ZZZ':
        current = nodes[current][rl[n % len(rl)] == 'R']
        n += 1
    print(n)

if __name__ == '__main__':
    main()
