# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    s = 0
    ahaha = dict(red = 12, green = 13, blue = 14)
    for line in slorp():
        g, rs = line.split(': ')
        no = False
        for r in rs.split('; '):
            for c in r.split(', '):
                n, C = c.split(' ')
                if int(n) > ahaha[C]:
                    no = True
        if not no:
            s += int(g.split(' ')[1])
    print(s)


if __name__ == '__main__':
    main()
    