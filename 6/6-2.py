#!/usr/bin/env python

# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    t = int(''.join(input().split()[1:]))
    d = int(''.join(input().split()[1:]))

    
    s = 0
    for x in range(t):
        s += x * (t - x) > d

    print(s)    

if __name__ == '__main__':
    main()
