# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())


# so I don't have any more accidentally global internal loop variables...
def main():
    s = 0
    for l in slorp():
    
        d = ''
        for c in l:
            if '0' <= c <= '9':
                d += c
        s += int(d[0]+d[-1])
    print(s)

if __name__ == '__main__':
    main()
