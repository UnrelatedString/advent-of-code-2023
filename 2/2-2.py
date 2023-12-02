# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    s = 0
    for line in slorp():
        g, rs = line.split(': ')
        mins = dict(red = 0, green = 0, blue = 0)
        for r in rs.split('; '):
            for c in r.split(', '):
                n, C = c.split(' ')
                mins[C] = max(mins[C], int(n))
        s += mins['red'] * mins['green'] * mins['blue']

        
    print(s)


if __name__ == '__main__':
    main()
    